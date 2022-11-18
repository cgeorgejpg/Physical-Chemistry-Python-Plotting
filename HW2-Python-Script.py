#Juan Yanes Benatuil

#Given Information
z_t = 0.3
z_o = 0.55
z_p = 0.1
z_b = 0.05

P = 2.0 #Bar

#Antoine Coefficients
A_t = 4.05043
B_t = 1327.62 
C_t = -55.525

A_o = 4.05075
B_o = 1356.36
C_o = -63.515

A_p = 3.97786
B_p = 1064.84
C_p = -41.136

A_b = 3.98523
B_b = 1184.24
C_b = -55.578

def BubblePointEq(T0):
    
    logPSatt = A_t - B_t / (T0 + C_t)
    PSatt = 10 ** (logPSatt)
    
    logPSato = A_o - B_o / (T0 + C_o)
    PSato = 10 ** (logPSato)
    
    logPSatp = A_p - B_p / (T0 + C_p)
    PSatp = 10 ** (logPSatp)
    
    logPSatb = A_b - B_b / (T0 + C_b)
    PSatb = 10 ** (logPSatb)
    
    K_t = PSatt / P
    K_o = PSato / P
    K_p = PSatp / P
    K_b = PSatb / P
    
    BubblePointVal = z_t / K_t + z_o / K_o + z_p / K_p + z_b / K_b
    
    return BubblePointVal

T0 = 435
T_tracker = []
for i in range(100000):

    if BubblePointEq(T0) > 1.01:
        if BubblePointEq(T0 + 0.1) > BubblePointEq(T0):
            T0 = T0 + 0.1
        else:
            T0 = T0 - 0.1
    if BubblePointEq(T0) < 0.99:
        if BubblePointEq(T0 + 0.1) > BubblePointEq(T0):
            T0 = T0 + 0.1
        else:
            T0 = T0 - 0.1
  
    T_tracker.append(T0)
    if len(T_tracker) > 2:
        if T_tracker[-2] == T_tracker[-1]:
            break
print('Optimized Temperature is:', round(T0,1))

    
logPSatt = A_t - B_t / (T0 + C_t)
PSatt = 10 ** (logPSatt)

logPSato = A_o - B_o / (T0 + C_o)
PSato = 10 ** (logPSato)

logPSatp = A_p - B_p / (T0 + C_p)
PSatp = 10 ** (logPSatp)

logPSatb = A_b - B_b / (T0 + C_b)
PSatb = 10 ** (logPSatb)

K_t = PSatt / P
K_o = PSato / P
K_p = PSatp / P
K_b = PSatb / P

x_tDew = round(z_t / (1 + (PSatt/P - 1)),3)
x_oDew = round(z_o / (1 + (PSato/P - 1)),3)
x_pDew = round(z_p / (1 + (PSatp/P - 1)),3)
x_bDew = round(z_b / (1 + (PSatb/P - 1)),3)

y_tDew = round(x_tDew * PSatt/P,3)
y_oDew = round(x_oDew * PSato/P,3)
y_pDew = round(x_pDew * PSatp/P,3)
y_bDew = round(x_bDew * PSatb/P,3)
    
print('x_t =', x_tDew, 'x_o =', x_oDew, 'x_p =',x_pDew, 'x_b =',x_bDew)
print('y_t =', y_tDew, 'y_o =', y_oDew, 'y_p =',y_pDew, 'y_b =',y_bDew)