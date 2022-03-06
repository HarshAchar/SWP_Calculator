# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:29:59 2022
Updated on 21-Feb-2022 by HarshAchar

@authors: SHANTANU, HarshAchar

"""
import json
import shutil
import uvicorn
import SWP_Main as swp
from fastapi import FastAPI, Body, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="./")

@app.get("/version")
async def get_version():
    '''
    SWP Calculaion Application
    '''
    
    try:
        with open("version.json") as f:
            return json.load(f)['info']
        
    except Exception as ex:
        print('read_root:Error', ex)
        return {'error':ex}
    
# =============================================================================
#     
# =============================================================================

@app.get("/index", response_class=HTMLResponse)
def write_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# =============================================================================
#     
# =============================================================================

@app.post("/swp", summary = "to compute SWP calculations")
async def compute_swp(request: Request, swp_amount: int = Form(...), investment: int = Form(...), investment_period: int = Form(...), RoR: int = Form(...), inflation: int = Form(...)):
    """
    Parameters
    ----------
    params : SWPVariables
        Computes SWP calculations as per the input years, interest rate, inflation swp-amount and for the initial investment.

    Returns
    -------
    A dataframe of SWP calculations.
    The year till the money lasts.
    The month till the money lasts.

    """

    try:
        swp_object = swp.SWPCalculator(swp_amount,
                                       investment,
                                       investment_period,
                                       RoR,
                                       inflation)
        
        output = swp_object.calculate_swp()
        if output is not None:
            return {'output':output}
        else:
            return {"output":None,'message':'Error in getting swp calculations'}
        
    except Exception as ex:
        print(ex)
        return {"output": None, 'message': "Error in getting swp calculations info.{0}".format(ex)}
    
# =============================================================================
# 
# =============================================================================

# if __name__ == '__main__':
#     uvicorn.run(debug=True)
