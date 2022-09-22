## Importaçõe
import smtplib
import email.message
from datetime import datetime
import streamlit as st  # Daskboard

def Robo():
    st.header('***Robô que envia email***')

    data_e_hora_atuais = datetime.now()
    data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    hora_em_texto = data_e_hora_atuais.strftime('%H:%M')

    emailuser = st.sidebar.text_input('Digite seu email', 'seuemail@gmail.com')

    st.markdown("<h3 style='color:#F00;'>Funcionalidades do Robo</h3>", unsafe_allow_html=True)
    st.write('O robo recebe o email digitado pelo usuario e envia um email com a data e a horas.')
    st.write(f'Hoje é dia: {data_em_texto}')
    st.write(f'E agora são: {hora_em_texto}')
    st.write('Para testar o robo basta digitar seu email no campo ao lado.')

    corpo_email = f"""
    <p>Hoje é dia: {data_em_texto}</p>
    <p>E agora são: {hora_em_texto}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Email Automático"
    msg['From'] = 'tamara.zoner@gmail.com'
    msg['To'] = emailuser
    password = 'twbpevvsbnbjhpnr'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    if emailuser != "seuemail@gmail.com":
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        st.markdown(f"<h3 style='color:#F00;'>Email enviado com suscesso para {emailuser} </h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    Robo()