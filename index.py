from Login import LoginValidator

# Rut con cuenta vista activa
rut = '49974450'
password = 'coop1234'
login = LoginValidator(rut, password)
login.access()