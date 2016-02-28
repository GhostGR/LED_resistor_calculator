# LED_resistor_calculator

### DESCRIPTION
     A python script that calculates the required resistor   
     and its wattage to make a LED run properly, using   
     the input voltage, the LED forward voltage and  
     the LED operating current.
  
### HOW TO USE
    1. Start the script
    2. Input the requested data
    
### VERSIONS
**V1.0** : This version contains the basic functioning script.
    
### FORMULAS USED
##### To calculate the resistor
    R = (Vin-Vled)/(Ima/1000)
    
    R    -> Led resistor(Ω)
    Vin  -> Power source voltage(V)
    Vled -> LED forward voltage(V)
    Ima  -> LED operating current(A)
#### To calculate the wattage
    Vin * (Ima/1000)
