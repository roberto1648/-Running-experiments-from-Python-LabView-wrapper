# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:58:45 2015

@author: Roberto
"""
import win32com.client

def runvi(vi_path = "",
          inputs = {},
          output_names = [],
          wait_for_completion = True):
    """
    run the vi specified by vi_path with the input 
    front panel objects specified by the inputs 
    dictionary and return a dictionary whose keys 
    are the strings given in output_names. 
    the vi_path can be copied from windows explorer 
    but paste it as raw text, e.g.: 
    
    vi_path = ,,,
    r"C:\folder\subfolder\some.vi".
    
    example:(vi_path points to a vi with a string 
    control or indicator called "String" and a 2D 
    array called "Array 2".)
    runvi(vi_path,{"String":'nooo', "Array 2": [[0, 1],[3,4]] }, ["String"])
    this doesn't care if either the inputs or 
    outputs are called controls or indicators by 
    labview.
    """
    # import win32com.client #load the interface
    labview =\
    win32com.client.Dispatch("Labview.Application") #get a ref to the Labview application
    
    VI = labview.getvireference(vi_path)#load the vi
    
    # set controls to given inputs:
    for name, value in inputs.iteritems():
        VI.setcontrolvalue(name, value)
        
    # run the vi:
    try:#have to do this,otherwise: TypeError: 'NoneType' object is not callable
        VI.Run(not wait_for_completion)#False=wait until vi finishes, True=don't wait
    except:
        pass
        
    # retrieve the outputs:
    outputs = {}
    for name in output_names:
        value = VI.getcontrolvalue(name)
        outputs[name] = value
        
    return outputs


def set_vi_values(vi_path = "",
                  inputs = {}):
    labview = \
        win32com.client.Dispatch("Labview.Application")  # get a ref to the Labview application

    VI = labview.getvireference(vi_path)  # load the vi

    # set controls to given inputs:
    for name, value in inputs.iteritems():
        VI.setcontrolvalue(name, value)


def get_vi_values(vi_path = "",
                   output_names = []):
    labview = \
        win32com.client.Dispatch("Labview.Application")  # get a ref to the Labview application

    VI = labview.getvireference(vi_path)  # load the vi

    # retrieve the outputs:
    outputs = {}
    for name in output_names:
        value = VI.getcontrolvalue(name)
        outputs[name] = value

    return outputs
