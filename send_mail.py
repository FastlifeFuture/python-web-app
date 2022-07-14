import smtplib
from email.mime.text import MIMEText

def send_mail(installer, date, region, site_name, site_number, type,address,city, county, state, zip_code, s_power_system_b, s_rects_conv_b, s_load_cap_b, s_load_current_b, s_dist_b, b_power_system_b, b_rects_conv_b, b_load_cap_b, b_load_current_b, b_dist_b, s_power_system_a, s_rects_conv_a, s_load_cap_a, s_load_current_a, s_dist_a, b_power_system_a, b_rects_conv_a, b_load_cap_a, b_load_current_a, b_dist_a, manufacturer_b, type_model_b, Sulf_gel_b, batteries_b, cells_b, runtime_b, manufacturer_a, type_model_a, Sulf_gel_a, batteries_a, cells_a, runtime_a):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'b4a8eeb3ff133c'
    password = '55358a871a1047'
    message = f'<h3> New Feedback Submision<h3><ul><lil>Installer: {installer}</li><lil>Date: {date}</li><lil>Region: {region}</li><lil>Site name: {site_name}</li><lil>Site Number: {site_number}</li><lil>Type: {type}</li><lil>Adress: {address}</li><lil>City: {city}</li><lil>County: {county}</li><lil>State: {state}</li><lil>Zip Code: {zip_code}</li><lil>24V Power System Model Before: {s_power_system_b}</li><lil>Quantity & Size of Rectifiers/Converters Before: {s_rects_conv_b}</li><lil>Total 24V Load Capacity (Amps) Before: {s_load_cap_b}</li><lil>Existing 24V Load Current (Amps) Before: {s_load_current_b}</li><lil>Available 24V distribution positions Before: {s_dist_b}</li><lil>48V Power System Model Before: {b_power_system_b}</li><lil>Quantity & Size of Rectifiers/Converters Before: {b_rects_conv_b}</li><<lil>Total 48V Load Capacity (Amps) Before: {b_load_cap_b}</li><lil>Existing 48V Load Current (Amps) Before: {b_load_current_b}</li><lil>Available 48V distribution positions Before: {b_dist_b}</li><lil>24V Power System Model After: {s_power_system_a}</li><lil>Quantity & Size of Rectifiers/Converters After : {s_rects_conv_a}</li><lil>Total 24V Load Capacity (Amps) After: {s_load_cap_a}</li><lil>Existing 24V Load Current (Amps) After: {s_load_current_a}</li><lil>Available 24V distribution positions After: {s_dist_a}</li><lil>48V Power System Model After: {b_power_system_a}</li><lil>Quantity & Size of Rectifiers/Converters After: {b_rects_conv_a}</li><<lil>Total 48V Load Capacity (Amps) After: {b_load_cap_a}</li><lil>Existing 48V Load Current (Amps) After: {b_load_current_a}</li><lil>Available 48V distribution positions After: {b_dist_a}</li><lil>Manufacturer Before: {manufacturer_b}</li><lil>Type/model Before: {type_model_b}</li><lil>sulfuric or gel type Before: {Sulf_gel_b}</li><lil># of batteries Before: {batteries_b}</li><lil># of cells Before: {cells_b}</li><lil>Run time based based existing load (hours) Before: {runtime_b}</li><lil>Manufacturer After: {manufacturer_a}</li><lil>Type/model After: {type_model_a}</li><lil>sulfuric or gel type After: {Sulf_gel_a}</li><lil># of batteries After: {batteries_a}</li><lil># of cells After: {cells_a}</li><lil>Run time based based existing load (hours) After: {runtime_a}</li></ul>'

    sender_email = 'travislucasdatatech@gmail.com'
    receiver_email = 'travis.lucas11@icould.com'
    msg  = MIMEText(message, 'html')
    msg['Subject'] = 'Pesa'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
