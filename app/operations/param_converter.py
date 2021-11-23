# import numpy as np
# line_array = params.flatten()  #  En caso de querer aplanar una matriz

def delta_param(array):  
    delta = array[0][0]*array[1][1] - array[0][1]*array[1][0]
    return delta

def delta_inverse(array):
    delta = array[0][1]*array[1][0] - array[0][0]*array[1][1]
    return delta

z0=50

y0=1/z0

# def delta_param(params):
#     det = np.linalg.det(params)
#     return int(det)

#####################   Z PARAMETERS    ########################

#   Z a Y (ready)

def z_to_y(params):

    delta = delta_param(params)
    i11 = params[1][1]/delta
    i12 = -params[0][1]/delta
    i21 = -params[1][0]/delta
    i22 = params[0][0]/delta
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   Z a T (ready)

def z_to_t(params):
    delta = delta_param(params)
    i11 = params[0][0]/params[1][0]
    i12 = delta/params[1][0]
    i21 = 1/params[1][0]
    i22 = params[1][1]/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   Z a ABCD (ready)

def z_to_abcd(params):

    delta = delta_param(params)
    i11 = params[0][0]/params[1][0]
    i12 = delta/params[1][0]
    i21 = 1/params[1][0]
    i22 = params[1][1]/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   Z a S (ready)

def z_to_s(params):

    delta = delta_param(params)
    i11 = ((params[0][0]-z0)*(params[1][1]+z0)-((params[0][1])*(params[1][0])))/((params[0][0]+z0)*(params[1][1]+z0)-((params[0][1])*(params[1][0])))
    i12 = (2*z0*params[0][1])/((params[0][0]+z0)*(params[1][1]+z0)-((params[0][1])*(params[1][0])))
    i21 = (2*z0*params[1][0])/((params[0][0]+z0)*(params[1][1]+z0)-((params[0][1])*(params[1][0])))
    i22 = ((params[0][0]+z0)*(params[1][1]-z0)-((params[0][1])*(params[1][0])))/((params[0][0]+z0)*(params[1][1]+z0)-((params[0][1])*(params[1][0])))
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#####################   Y PARAMETERS    ########################

#   Y a Z (ready)

def y_to_z(params):

    delta = delta_param(params)
    i11 = params[1][1]/delta
    i12 = -params[0][1]/delta
    i21 = -params[1][0]/delta
    i22 = params[0][0]/delta
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   Y a T (ready)

def y_to_t(params):
    delta = delta_param(params)
    i11 = -params[1][1]/params[1][0]
    i12 = -1/params[1][0]
    i21 = -delta/params[1][0]
    i22 = -params[0][0]/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   Y a ABCD (ready)

def y_to_abcd(params):

    delta = delta_inverse(params)
    i11 = -params[1][1]/params[1][0]
    i12 = -1/params[1][0]
    i21 = delta/params[1][0]
    i22 = -params[0][0]/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   Y a S (ready)

def y_to_s(params):

    delta = delta_param(params)
    i11 = ((y0-params[0][0])*(y0+params[1][1])+((params[0][1])*(params[1][0])))/((params[0][0]+y0)*(params[1][1]+y0)-((params[0][1])*(params[1][0])))
    i12 = (-2*y0*params[0][1])/((params[0][0]+y0)*(params[1][1]+y0)-((params[0][1])*(params[1][0])))
    i21 = (-2*y0*params[1][0])/((params[0][0]+y0)*(params[1][1]+y0)-((params[0][1])*(params[1][0])))
    i22 = ((y0+params[0][0])*(y0-params[1][1])-((params[0][1])*(params[1][0])))/((params[0][0]+y0)*(params[1][1]+y0)-((params[0][1])*(params[1][0])))
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#####################   T PARAMETERS    ########################

#   T a Z (ready)

def t_to_z(params):

    delta = delta_param(params)
    i11 = params[0][0]/params[1][0]
    i12 = delta/params[1][0]
    i21 = 1/params[1][0]
    i22 = params[0][0]/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   T a Y (ready)

def t_to_y(params):
    delta = delta_param(params)
    i11 = -params[1][1]/params[0][1]
    i12 = -delta/params[0][1]
    i21 = -1/params[0][1]
    i22 = params[0][0]/params[0][1]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   T a ABCD


#   T a S (ready)

def t_to_s(params):

    delta = delta_param(params)
    i11 = params[1][0]/params[0][0]
    i12 = delta/params[0][0]
    i21 = 1/params[0][0]
    i22 = -params[0][1]/params[0][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#####################   ABCD PARAMETERS    ########################

#   ABCD a Z (ready)

def abcd_to_z(params):

    delta = delta_param(params)
    i11 = params[0][0]/params[1][0]
    i12 = delta/params[1][0]
    i21 = 1/params[1][0]
    i22 = params[0][0]/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   ABCD a T


#   ABCD a Y (ready)

def abcd_to_y(params):

    delta = delta_inverse(params)
    i11 = params[1][1]/params[0][1]
    i12 = delta/params[0][1]
    i21 = -1/params[0][1]
    i22 = params[0][0]/params[0][1]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   ABCD a S (ready)

def abcd_to_s(params):

    delta = delta_inverse(params)
    i11 = (params[0][0]+(params[0][1]/z0)-(z0*params[1][0])-params[1][1])/(params[0][0]+(params[0][1]/z0)+(z0*params[1][0])-params[1][1])
    i12 = (2*delta)/(params[0][0]+(params[0][1]/z0)+(z0*params[1][0])-params[1][1])
    i21 = 2/(params[0][0]+(params[0][1]/z0)+(z0*params[1][0])-params[1][1])
    i22 = (-params[0][0]+(params[0][1]/z0)-(z0*params[1][0])-params[1][1])/(params[0][0]+(params[0][1]/z0)+(z0*params[1][0])-params[1][1])
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params


#####################   S PARAMETERS    ########################

#   S a Z (ready)

def s_to_z(params):

    delta = delta_param(params)
    det = ((1-params[0][0])*(1-params[1][1])-((params[0][1])*(params[1][0])))
    i11 = z0*((1+params[0][0])*(1-params[1][1])+((params[0][1])*(params[1][0])))/det
    i12 = z0*2*(params[0][1])/det
    i21 = z0*2*(params[1][0])/det
    i22 = z0*((1-params[0][0])*(1+params[1][1])+((params[0][1])*(params[1][0])))/det
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   S a T (ready)

def s_to_t(params):

    delta = delta_inverse(params)
    i11 = 1/params[1][0]
    i12 = -params[1][1]/params[1][0]
    i21 = params[0][0]/params[1][0]
    i22 = delta/params[1][0]
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   S a Y (ready)

def s_to_y(params):
    delta = delta_param(params)
    i11 = y0*((1-params[0][0])*(1+params[1][1])+((params[0][1])*(params[1][0])))/(((1+params[0][0])*(1+params[1][1]))-((params[0][1])*(params[1][0])))
    i12 = (y0*-2*(params[0][1]))/(((1+params[0][0])*(1+params[1][1]))-((params[0][1])*(params[1][0])))
    i21 = (y0*-2*(params[1][0]))/(((1+params[0][0])*(1+params[1][1]))-((params[0][1])*(params[1][0])))
    i22 = y0*((1+params[0][0])*(1-params[1][1])+((params[0][1])*(params[1][0])))/(((1+params[0][0])*(1+params[1][1]))-((params[0][1])*(params[1][0])))
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#   S a ABCD (ready)

def s_to_abcd(params):

    delta = delta_param(params)
    i11 = ((1+params[0][0])*(1-params[1][1])+((params[0][1])*(params[1][0])))/(2*params[1][0])
    i12 = z0*((1+params[0][0])*(1+params[1][1])+((params[0][1])*(params[1][0])))/(2*params[1][0])
    i21 = y0*((1-params[0][0])*(1-params[1][1])+((params[0][1])*(params[1][0])))/(2*params[1][0])
    i22 = ((1-params[0][0])*(1+params[1][1])+((params[0][1])*(params[1][0])))/(2*params[1][0])
    array_params = (
        str(i11),
        str(i12),
        str(i21),
        str(i22)
    )
    return array_params

#####################   Select Convertion   ########################

def converter(input, output, values):
    #           FROM Z
    if input == 'z' and output == 'y':
        return z_to_y(values)
    elif input == 'z' and output == 'abcd':
        return z_to_abcd(values)
    elif input == 'z' and output == 's':
        return z_to_s(values)
    elif input == 'z' and output == 't':
        return z_to_t(values)
    
    #           FROM Y
    elif input == 'y' and output == 'z':
        return y_to_z(values)
    elif input == 'y' and output == 'abcd':
        return y_to_abcd(values)
    elif input == 'y' and output == 's':
        return y_to_s(values)
    elif input == 'y' and output == 't':
        return y_to_t(values)
    
    #           FROM ABCD
    elif input == 'abcd' and output == 'z':
        return abcd_to_z(values)
    elif input == 'abcd' and output == 'y':
        return abcd_to_y(values)
    elif input == 'abcd' and output == 's':
        return abcd_to_s(values)

    #           FROM S
    elif input == 's' and output == 'z':
        return s_to_z(values)
    elif input == 's' and output == 'y':
        return s_to_y(values)
    elif input == 's' and output == 'abcd':
        return s_to_abcd(values)
    elif input == 's' and output == 't':
        return s_to_t(values)

    #           FROM T
    elif input == 't' and output == 'z':
        return t_to_z(values)
    elif input == 't' and output == 'y':
        return t_to_y(values)
    elif input == 't' and output == 's':
        return t_to_s(values)
    else:
        return 0


#           testing Menu            
def menu():
    params = [[50, 4 - 3j], [30, 44]]
    print(f"""
    *************************************************************************************
            **** Bienvenido a la seccion de Pruebas del convertidor ****
            Para poder probar las funciones, inserta con minusculas 
            las letras de los parametros cuando se te pidan.
    *************************************************************************************
    """)
    entrada = input(f"¿Que tipo de parametro ingresaras? (z, y, abcd, s o t) ")
    salida = input(f"¿En que tipo de parametro quieres que se convierta? (z, y, abcd, s o t) ")
    results =  converter(entrada, salida, params)

    if(results == 0):
        print("Por favor inserte un valor valido ")
        menu()
    else:
        print(results)
        a = input("Seguimos haciendo convirtiendo [s/n] ")
        if a == "s":
            menu() 
        elif a == "n":
            print("Adios")

#####################   TESTING    ########################

if __name__ == '__main__': 
    menu()




# z_to_abcd and z_to_y and z_to_t ready
# y_to_z and y_to_abcd and t_to_t ready
# abcd_to_z and abcd_to_y and abcd_to_s ready

# abcd_to_t not exist for are equals

#  test results : s_to_y and s_to_z and s_to_abcd and z_to_s and y_to_s issues