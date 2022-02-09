# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:29:59 2022

@author: SHANTANU
"""

import json
import shutil
import uvicorn
import SWP_Main as swp
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

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

class SWPVariables(BaseModel):
    swp_amount:int
    investment:int
    investment_period:int
    RoR:int
    inflation:int
    
# =============================================================================
#     
# =============================================================================
@app.post("/swp", summary = "to compute SWP calculations")
async def compute_swp(params: SWPVariables):
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
        
        
        swp_object = swp.SWPCalculator(params.swp_amount,
                                       params.investment,
                                       params.investment_period,
                                       params.RoR,
                                       params.inflation)
        
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

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
        
