import json
import math
import logging

logging.basicConfig(level=logging.INFO, format=' %(levelname)s: %(message)s')


def calc_turbidity(calibration: float, detector: float) -> float:
    """
    Given two floats, this function multiplies them together to calculate the turbidity.

    Args:
        calibration (float): the calibration constant.
        detector (float): the ninety degree detector current.

    Results:
        t (float): the turbidity of the water
    """

    t = calibration * detector
    return(t)
    

def time_till_safe(t0: float, d: float, NTU: float) -> float:
    """
    given three floats, this function will calculate the time until the water is safe to drink. 
    
    Args:
        t0 (float): the current turbidity of the water.
        d (float): the decay fator per hour, expressed as a decimal.
        NTU (float): the turbidity threshold for safe water.

    Calculation explanation: 
        math.log is just the natural log
        so time = ln(NTU/t0)/ln(-(d-1))

    Returns:
        time (float): the total time required until the water is considdered safe to drink (below the NTU threshold)
    """   
    time = (math.log(NTU/t0))/math.log(-(d-1))     
    
    return(time)


def main():

    iterator = 0
    
    #initialize turbidity
    turb = 0
    #set the decay rate
    d = 0.02
    #set the safe threshold
    NTU = 1.0


    with open('turbidity_data.json', 'r') as f:
        turb_data = json.load(f)
    
    
    for row in list(reversed(list(turb_data['turbidity_data'])))[0:5]:
        turb = turb + calc_turbidity(float(row['calibration_constant']), float(row['detector_current']))
        iterator = iterator + 1
    
    average_turb = turb/iterator

    time = time_till_safe(average_turb, d, NTU)
    
    if (average_turb > 1):
        print("Average turbidity based on most recent five measurements =", average_turb, "NTU") 
        logging.warning('Turbidity is above threshold for safe use') 
        print ("Minimum time required to return below a safe threshold =", time, "hours")
    
    if (average_turb <= 1):
           
        print("Average turbidity based on most recent five measurements =", average_turb, "NTU") 
        logging.info('Turbidity is below threshold for safe use')        
        print ("Minimum time required to return below a safe threshold = 0 hours")
    

if __name__ == '__main__':
    main()
    

