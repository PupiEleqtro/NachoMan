import pytest

# Creado por PupiEleqtro.
# formula utilizada: (Dia + Tabla_Mes + Año + (Año // 4) + Tabla_Siglo) % 7
# Año: Se utilizan los ultimos 2 digitos, por ejemplo: de 2015 seria 15. 
# Video donde encontre esta formula: https://www.youtube.com/watch?v=793rAtaorCM
#-------------------------------------------------------------------------------


# Representaremos si el año es bisiesto o no, si el mismo es divisible entre 4.
# bisiesto: Int -> Bool
# Recibe el año y devuelve true si el año es bisiesto o false en caso de que no
# lo fuera.
# Entrada: 2020; Salida: True.
# Entrada: 2015; Salida: False.
# Entrada: 2009; Salida: False.
def bisiesto(año):
    """Recibe el año y determina si el mismo es bisiesto o no."""
    if año % 4 == 0:
        return True
    else:
        return False

def test_bisiesto():
    assert bisiesto(2020) == True
    assert bisiesto(2015) == False
    assert bisiesto(2009) == False

# Representaremos la tabla en el siguiente orden:
# * Enero : 0; Febrero: 3; Marzo: 3; Abril: 6; Mayo: 1; Junio: 4; Julio: 6;
# * Agosto: 2; Septiembre: 5; Octubre: 0; Noviembre: 3; Diciembre: 5.
# TablaIntervMes: Int -> Int
# Toma un mes y devuelve que intervalo es deacuerdo a la tabla.
# Entrada: 3; Salida: 3.
# Entrada: 4; Salida: 6.
# Entrada: 12; Salida: 5.
def TablaIntervMes(mes):
    """Deacuerdo al mes ingresado determina que intervalo es deacuerdo a la tabla."""
    if mes == 1:
        return 0
    elif mes == 2:
        return 3
    elif mes == 3:
        return 3
    elif mes == 4:
        return 6
    elif mes == 5:
        return 1
    elif mes == 6:
        return 4
    elif mes == 7:
        return 6
    elif mes == 8:
        return 2
    elif mes == 9:
        return 5
    elif mes == 10:
        return 0
    elif mes == 11:
        return 3
    elif mes == 12:
        return 5

def test_TablaIntervMes():
    assert TablaIntervMes(3) == 3
    assert TablaIntervMes(4) == 6
    assert TablaIntervMes(12) == 5

# Representaremos la tabla en el siguiente orden:
# [1200, 1299]: 6; [1300, 1399]: 5; [1400, 1499]: 4; [1500, 1582]: 3;
# [1583, 1599]: 0; [1600, 1699]: 6; [1700, 1799]: 4; [1800, 1899]: 2;
# [1900, 1999]: 0; [2000, 2099]: 6; [2100, 2199]: 4; [2200, 2299]: 2.
# TablaIntervAño: Int -> Int
# Toma el año y devuelve el intervalo deacuerdo a la tabla.
# Entrada: 2000; Salida: 6.
# Entrada: 1845; Salida: 2.
# Entrada: 1577; Salida: 3.
def TablaIntervAño(año):
    """Deacuerdo al año devuelve el intervalo de la tabla"""
    if año >= 1200 and 1299 >= año:
        return 6
    elif año >= 1300 and 1399 >= año:
        return 5
    elif año >= 1400 and 1499 >= año:
        return 4
    elif año >= 1500 and 1582 >= año:
        return 3
    elif año >= 1583 and 1599 >= año:
        return 0
    elif año >= 1600 and 1699 >= año:
        return 6
    elif año >= 1700 and 1799 >= año:
        return 4
    elif año >= 1800 and 1899 >= año:
        return 2
    elif año >= 1900 and 1999 >= año:
        return 0
    elif año >= 2000 and 2099 >= año:
        return 6
    elif año >= 2100 and 2199 >= año:
        return 4
    elif año >= 2200 and 2299 >= año:
        return 2

def test_TablaIntervAño():
    assert TablaIntervAño(2000) == 6
    assert TablaIntervAño(1845) == 2
    assert TablaIntervAño(1577) == 3

# Representaremos la tabla en el siguiente orden:
# Lunes: 1; Martes: 2; Miercoles: 3; Jueves: 4; Viernes: 5; Sabado: 6;
# Domingo: 0.
# TablaIntervDia: Int -> Str
# Toma la formula para sacar el dia de la semana y deacuerdo al valor dado
# entrega que intervalo de l dia de la semana es
# Entrada: 1; Salida: "Lunes".
# Entrada: 0; Salida: "Domingo".
# Entrada: 4; Salida: "Jueves".
def TablaIntervDia(dia):
    """Saca que dia de la semana es deacuerdo a la formula del dia de la semana."""
    if dia == 0:
        return "Domingo"
    elif dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miercoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sabado"

def test_TablaIntervDia():
    assert TablaIntervDia(1) == "Lunes"
    assert TablaIntervDia(0) == "Domingo"
    assert TablaIntervDia(4) == "Jueves"


# Representaremos los dias de la semana mediante tupla y la fecha tambien.
# diasSem: Tuple -> Str
# Toma el dia, el mes y año, devuelve un string que determina el dia de la
# semana en la fecha indicada.
# Entrada: (20, 2, 2019); Salida: "Miercoles".
# Entrada: (29, 9, 2020); Salida: "Martes".
# Entrada: (31, 12, 1999); Salida: "Viernes".
def diasSem(fecha):
    """Deacuerdo al dia, mes y año, entrega un string indicando el dia de la semana."""
    dia = fecha[0]
    mes = fecha[1]
    año = fecha[2]
    mesIntervalo = TablaIntervMes(mes)
    añoIntervalo = TablaIntervAño(año)
    formula = (dia + mesIntervalo + int(str(año)[2:4]) + (int(str(año)[2:4])) // 4 + añoIntervalo) % 7 
    diaIntervalo = TablaIntervDia(formula)
    return diaIntervalo

def test_diasSem():
    assert diasSem((20, 2, 2019)) == "Miercoles"
    assert diasSem((29, 9, 2020)) == "Martes"
    assert diasSem((31, 12, 1999)) == "Viernes"

# Representaremos el dia despues como el dia que le sigue al dado. Las fechas
# estaran representadas como tuplas, siguiendo este orden:
# (Dia, Mes, Año)
# diaDespues: Tuple -> Tuple
# Toma el dia y entrega el dia que le sigue al dado.
# Entrada: (31, 12, 2000); Salida: (1, 1, 2001).
# Entrada: (28, 2, 1996); Salida: (29, 2, 1996).
# Entrada: (28, 2, 2011); Salida: (1, 3, 2011).
def diaDespues(fecha):
    """Dado el dia entrega el dia siguiente"""
    dia = fecha[0]
    mes = fecha[1]
    año = fecha[2]
    if bisiesto(año) == True:
        if mes == 12 and dia == 31:
            fechaDesp = (1, 1, año+1)
            return fechaDesp
        elif ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia == 31) or (mes == 2 and dia == 29) or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 30):
            fechaDesp = (1, mes+1, año)
            return fechaDesp
        else:
            fechaDesp = (dia+1, mes, año)
            return fechaDesp
    else:
        if mes == 12 and dia == 31:
            fechaDesp = (1, 1, año+1)
            return fechaDesp
        elif ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia == 31) or (mes == 2 and dia == 28) or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 30):
            fechaDesp = (1, mes+1, año)
            return fechaDesp
        else:
            fechaDesp = (dia+1, mes, año)
            return fechaDesp
            

def test_diaDespues():
    assert diaDespues((31, 12, 2000)) == (1, 1, 2001)
    assert diaDespues((28, 2, 1996)) == (29, 2, 1996)
    assert diaDespues((28, 2, 2011)) == (1, 3, 2011)

# Representaremos cada mes como los meses del año:
# Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre,
# Noviembre, Diciembre.
# cualMesEs: Int -> Str
# Toma el numero del mes y entrega el nombre del mes.
# Entrada: 1; Salida: "Enero".
# Entrada: 12; Salida: "Diciembre".
# Entrada: 9; Salida: "Septiembre".
def cualMesEs(mes):
    """Dado el numero del mes entega el nombre del mismo."""
    if mes == 1:
        return "Enero"
    elif mes == 2:
        return "Febrero"
    elif mes == 3:
        return "Marzo"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Mayo"
    elif mes == 6:
        return "Junio"
    elif mes == 7:
        return "Julio"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Septiembre"
    elif mes == 10:
        return "Octubre"
    elif mes == 11:
        return "Noviembre"
    elif mes == 12:
        return "Diciembre"

def test_cualMesEs():
    assert cualMesEs(1) == "Enero"
    assert cualMesEs(12) == "Diciembre"
    assert cualMesEs(9) == "Septiembre"




# Representremos la fecha como un string, donde el usuario tendra que ingresarla.
# diaSiguienteT: Str -> Str.
# Toma la fecha y entrega la fecha ingresada con el dia de la semana que es,
# como tambien el mes que es y otra fecha del el dia posterior al ingresado,
# detallando tambien el dia.
# Entrada: 27/4/2000; Salida: "Hoy: Jueves 27 de Abril del 2000"
#                             "2000: Este año es bisiesto!!!"
#                             "Mañana: Viernes 28 de Abril del 2000".

# Entrada: 29/2/2008; Salida: "Hoy: Sabado 29 de Febrero del 2008"
#                             "2008: Este año es bisiesto!!!"
#                             "Mañana: Domingo 1 de Marzo del 2008".

# Entrada: 31/12/2013; Salida: "Hoy: Martes 31 de Diciembre del 2013"
#                              "Mañana: Miercoles 1 de Enero del 2014".
def dia():
    print("CUIDADO: NO INGRESE 0 DELANTE DE LOS NUMEROS ENTEROS.")
    print("Ingrese su fecha en el siguiente orden: Dia/Mes/Año.")
    f = input("Ingrese la fecha: ").split("/")
    fecha = ()
    for elemento in f:
        fecha += int(elemento),
    dia = fecha[0]
    mes = fecha[1]
    año = fecha[2]
    dia_Sem = diasSem(fecha)
    mes_Nom = cualMesEs(mes)
#----↑Fecha-------↓Fecha siguiente-------
    fechaDiaDesp = diaDespues(fecha)
    diaDesp = fechaDiaDesp[0]
    mesDesp = fechaDiaDesp[1]
    añoDesp = fechaDiaDesp[2]
    diaDesp_Sem = diasSem(fechaDiaDesp)
    mesDesp_Nom = cualMesEs(mesDesp)
    if bisiesto(año) == True:
        print(" Hoy :", dia_Sem, dia, "de", mes_Nom, "del", año, "\n", año, ": Este año es bisiesto!!!\n Mañana :", diaDesp_Sem, diaDesp, "de", mesDesp_Nom, "del", añoDesp)
    else:
        print(" Hoy :", dia_Sem, dia, "de", mes_Nom, "del", año, "\n Mañana :", diaDesp_Sem, diaDesp, "de", mesDesp_Nom, "del", añoDesp)
