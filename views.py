#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:27:40 2021

@author: thiago
"""
import os
import json 
from flask import render_template
from flask import Flask, request, jsonify, send_from_directory, abort,flash,redirect,url_for,session
from flask import Flask, render_template
import requests
import sqlite3
f = open('login_mdp.json')
global data
data = json.load(f)
f.close()
app = Flask(__name__)
app.config["DEBUG"] = True
image_folder = os.path.join('static', 'images')
app.config["IMAGES"] = image_folder







@app.route('/')
def home():
    user={'login' : 'Chancelle', 'surname':'Kizima'}
    chemin = os.path.join(app.config["IMAGES"], "photo.png")
    if session=={}:
        return render_template("home.html", title='Bienvenu', utilisateur=user)
    else :
        return render_template('home.html', title=str(session['login']), utilisateur=user)
    
    
@app.route('/Patient')#,methods=["POST"]

def Patient():
    
    
    
    
  
    return render_template( 'Connecter.html') #,Patient=info_patient,   Medecin=info_medecin,   Organisation=info_organisation,Medication=Medication)





# @app.route('/Patient')#,methods=["POST"]
# def Patient():
#     identifiant = request.args.get("id")
    
#     Organisation =  'fhir/Organization/0.json'
#     info_organisation = json.load(open(Organisation))
#     open(Organisation).close()
    
#     Patient = 'fhir/Patient/'+str(identifiant)+'.json'
#     info_patient = json.load(open(Patient))
#     open(Patient).close()
    
    
#     #Medecin = 'fhir/Medecin/'+str(identifiant)+'.json'
#     Medecin = 'fhir/Medecin/19765.json'
#     info_medecin = json.load(open(Medecin))
#     open(Medecin).close()
    
   
   

#     MedicationRequest = 'fhir/MedicationRequest/19765.json'
#     Medication = json.load(open(MedicationRequest))
  
#     return render_template( 'Connecter.html',Patient=info_patient,   Medecin=info_medecin,   Organisation=info_organisation,Medication=Medication)













@app.route('/Medecin')#,methods=["POST"]
def medecin():
    identifiant = request.args.get("id")
    Organisation =  'fhir/Organization/0.json'
    info_organisation = json.load(open(Organisation))
    open(Organisation).close()
    Patient = 'fhir/Patient/'+str(identifiant)+'.json'
    info_patient = json.load(open(Patient))
    open(Patient).close()
    
    
    Medecin = 'fhir/Medecin/'+str(identifiant)+'.json'
    info_medecin = json.load(open(Medecin))
    open(Medecin).close()

   

    MedicationRequest = 'fhir/MedicationRequest/'+str(identifiant)+'.json'
    Medication = json.load(open(MedicationRequest))
   


    # mail1 = str(request.args.get('Id'))
    # fichier="fhir/Pro"+mail1+".json"
    # var=open(fichier)
    # charge=json.load(var)
    # var.close()


    # mail2 = str(request.args.get('Id'))
    # fichier2="fhir/Pro"+mail2+".json"
    # var2=open(fichier2)
    # charge=json.load(var2)
    # var2.close()


    # mail3 = str(request.args.get('Id'))
    # fichier3="fhir/Pro"+mail3+".json"
    # var3=open(fichier3)
    # charge3=json.load(var3)
    # var3.close()
    return render_template('Medecin.html', medecin=info_medecin, Patient=info_patient,   Medecin=info_medecin,   Organisation=info_organisation,Medication=Medication)




@app.route('/Signin',methods=["POST"])
def Signin():
    if request.method == 'POST':
        login = request.form['login']
        mdp = request.form['mdp']
        valid_member=False
        
        conn= sqlite3.connect ( 'database.db')
        

        # print("Base de données ouverte avec succès")

        # conn.execute( 'CREATE TABLE member(login TEXT, mdp TEXT )')

        # print("Table créée avec succès")

        # conn.close()
        
        
        with sqlite3.connect("database.db") as con:
            cur= con.cursor()
            cur.execute("INSERT INTO member(login,mdp) VALUES (?,?)", (" chancelle","1234"))
            con.commit()
        con.close()

        
        with sqlite3.connect("database.db") as con:
            cur= con.cursor()
            cur.execute("SELECT * FROM member")
            a=cur.fetchall()
            print(a)
            return render_template('Authentification.html', title='Authentification Réussi!')
        con.close()
    
    
        for i in data["member"]:
            if i["login"]==login and i["mdp"]==mdp:
                valid_member=True
                session['login']=login
                session['mdp']=mdp
        if valid_member==True:
            return render_template('Authentification.html', title='Authentification Réussi!')
        else: 
            return render_template('Erreur.html', title='Erreur')
        
        
        
              
@app.route('/Authentification')
def authentification():
    return render_template('Authentification.html', title='Authentification Réussi!')

@app.route('/Erreur')
def errer():
    return render_template('Erreur.html', title='Erreur')

@app.route('/Joindre')
def join():
    if session=={}:
        return render_template('Joindre.html', title='Join')
    else :
        return render_template('Joindre_connecter.html', title='Connecter')

@app.route('/Register',methods=["POST"])

def Register():
    if request.method == 'POST':
     
            
        login = request.form['login']
        mdp = request.form['mdp']
        member={ "login": login, "mdp":mdp}
        f = open('login_mdp.json','w')
        data["member"].append(member)
        json.dump(data,f)
        f.close()
        return render_template('Connecter.html', title='Connecter')




@app.route('/About')
def about():
    return render_template('About.html', title='About')

@app.route('/Deconnecter')#,methods=["POST"]
def deconnecter():
    session.pop('login',None)
    session.pop('mdp',None)
    return render_template('home.html', title='Bienvenu')














# @app.route("/confirmation",methods=['GET','POST'])
# def informations_patient():    
#     identifiant = request.form.get('identifier')
#     nom = request.form.get('name')
#     genre = request.form.get('gender')
#     date = request.form.get('birthDate')
#     adresse = request.form.get('address')
#     covid = request.form.get('covid')
#     dtp = request.form.get('dtp')
#     coqueluche = request.form.get('Coqueluche')
#     rubeole=request.form.get('Rubeole')
#     hepatite=request.form.get('Hepatite')
#     rougeole=request.form.get('Rougeole')
#     oreillons=request.form.get('Oreillons')

#     patient = {
#               "resourceType" : "Patient",
#               "identifier" : identifiant,
#               "active" : "<boolean>",
#               "name" : nom,
#               "telecom" : "[{ ContactPoint }]",
#               "gender" : genre,
#               "birthDate" : date,
#               "deceasedBoolean" : "<boolean>",
#               "deceasedDateTime" : "<dateTime>",
#               "address" : adresse,
#               "maritalStatus" : "{ CodeableConcept }",
#               "multipleBirthBoolean" : "<boolean>",
#               "multipleBirthInteger" : "<integer>",
#               "photo" : "[{ Attachment }]",
#               "contact" : [{
#                 "relationship" : "[{ CodeableConcept }]",
#                 "name" : "{ HumanName }",
#                 "telecom" : "[{ ContactPoint }]",
#                 "address" : "{ Address }",
#                 "gender" : "<code>",
#                 "organization" : "{ Reference(Organization) }",
#                 "period" : "{ Period }"
#               }],
#               "communication" : [{
#                 "language" : "{ CodeableConcept }",
#                 "preferred" : "<boolean>"
#               }],
#               "generalPractitioner" : "[{ Reference(Organization|Practitioner|PractitionerRole) }]",
#               "managingOrganization" : "{ Reference(Organization) }",
#               "link" : [{ 
#                 "other" : "{ Reference(Patient|RelatedPerson) }",
#                 "type" : "<code>"
#               }]
#             }
#     with open("fhir/Patient/"+str(identifiant)+".json", "w") as f_write:
#         json.dump(patient, f_write, indent=2)
        
#     Vaccins = {
#         "Covid" : covid,
#         'DTP' : dtp,
#         'Coqueluche': coqueluche,
#         'Rubeole' : rubeole,
#         'Hepatite': hepatite,
#         'Rougeole' : rougeole,
#         'Oreillons' : oreillons
#         }
        
#     with open("fhir/Vaccins/"+str(identifiant)+".json", "w") as f_write:
#         json.dump(Vaccins, f_write, indent=2)
    
#     #return ("<a href='/'>Page principale</a>")
    
    
    


#     return render_template("infoperso.html")

#     #return render_template("home.html",charge=charge, charge2=charge2, charge3=charge3












































# @app.route('/infoperso', methods=['GET', 'POST'])
# def inscriptionpatient():
#     Mail = str(request.args.get('id')) 
#     username = request.args.get('Username')
#     mail=request.args.get('Mail')
#     DateNaissance=request.args.get('DateNaiss')
#     Mdp=request.args.get('Mdp')

    
    
#     donne = {}
#     fichier = "fhir/infoperso/"+ str(Mail)+".json"
#     if Mdp !=None:
#         donne = {
            
            
    
#             "resourceType" : "Patient",
           
#             "username" : str(username),
#             "Mail":str(Mail),
#             "DateNaissance":str(DateNaissance),
#             "Mdp": str(securite(Mdp)),
            
#             "organization" : "/fhir/Organization?_id="+ str(Mail)
#         }
#     with open(fichier, "w") as fichier_edite :
#         json.dump(donne, fichier_edite, indent=2)
#     var = open(fichier)
#     charge = json.load(var)
#     var.close()
    
# def securite (Mdp):   
#     objet = hashlib.md5(Mdp.encode())
    
#     return (objet.hexdigest())












# sender_email="E_sant_live.episen.com"
# password="vitrygtr"
# Mail = str(request.args.get('id')) 

# msg="Bienvenu sur E_santé_Live,"
# if Mail != None:
#      server = smtplib.SMTP("smtp.gmail.com",587)
#      server.starttls()
#      server.login(sender_email,password)
#      server.sendmail(sender_email,Mail,msg)
     
# return render_template("InscriptionPatient.html", charge=charge)

































# @app.route('/PatientConnecter', methods=['GET'])
# def connexionpatient():
#     global Mail
#     Mail = str(request.args.get('Mail'))
#     Mdp=request.args.get('Mdp')
#     fichier = "fhir/Patient/"+ Mail+".json"
#     var = open(fichier)
#     charge = json.load(var)
#     var.close()
#     if Mdp!=None:
#         if securite(Mdp) == charge['Mdp']:
#             return(sessionPatient())
#     return render_template("PatientConnecter.html", charge=charge)



# @app.route('/Patient', methods=['GET','POST'])
# def sessionPatient():
#     fichier="fhir/Patient/" +Mail + ".json"
#     var= open(fichier)
#     charge=json.load(var)
#     return render_template('sessionPatient.html',charge=charge)































# @app.route('/infoperso', methods=['GET'])
# def infoPatient():
#     ident = str(request.args.get('Id'))
#     nom = request.args.get('Nom')
#     prenom=request.args.get('Prenom')
#     age=request.args.get('Age')
#     sexe=request.args.get('Sexe')
#     mail=request.args.get('Mail')
#     tel=request.args.get('Telephone')

    
#     fichier = "fhir/Patient/"+ ident +".json"
#     donne = {
#       "resourceType" : "Patient",
#       "Id":str(ident),
#       "Nom" : str(nom),
#       "Prenom" : str(prenom),
#       "Age" : str(age),
#       "Sexe": str(sexe),
#       "Mail": str(mail),
#       "Telephone": str(tel),
#       "organization" : "/fhir/Organization?_id="+ ident
#     }
#     with open(fichier, "w") as fichier_edite :
#         json.dump(donne, fichier_edite, indent=2)
#     var = open(fichier)
#     charge = json.load(var)
#     var.close()

#     return render_template("infoperso.html", charge=charge)

















#     fichier2 = "fhir/Immunization/"+ ident +".json"
#     var2 = open(fichier2)
#     charge2 = json.load(var2)
#     var2.close()
    
#     fichier3 = "fhir/Medicamment/"+ident +".json"
#     var3 = open(fichier3)
#     charge3 = json.load(var3)
#     var3.close()    
#     return render_template("home.html",charge=charge, charge2=charge2, charge3=charge3)






















@app.route('/Accesinfopatient')#,methods=["POST"]
def accesinfopatient():
    recherche = str(request.args.get("recherche"))
    fichier="fhir/Patient/"+ recherche +".json"   
    var = open(fichier)
    charge = json.load(var)
    var.close()
    
    
    recherche2 = request.args.get("recherche2")
    Medicamment = str(request.args.get("Medicamment"))
    Dosage =  str(request.args.get("Dosage"))
    Note =  str(request.args.get("Note"))
    
    fichier2="fhir/Medicamment/"+str( recherche2) +".json"
    donne2 = {
        
        
        
        "resourceType" :"Medication Request",
        
        "Medicamment" : str(Medicamment),
        "Dosage" : str(Dosage),
        "Note" : str(Note),
        "organization" : "/fhir/Organization?_id="+ str(recherche2)
    }
    with open(fichier2, "w") as fichier2_edite :
        json.dump(donne2, fichier2_edite, indent=2)
    var2 = open(fichier2)
    charge2 = json.load(var2)
    var2.close()
    
    
    c=canvas.Canvas("fhir\Ordonnance\Ordonnance.pdf")
    c.drawString(100,100, Medicamment + Dosage + Note)
    c.showPage()
    c.save()
    
    sender_email="Santé_Live.episen.com"
    password="vitrygtr"
    message="Bonjour, \n\Vous trouverez ci-joint votre ordonnance. "
    
    if recherche2!=None:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recherche2,message)
    return render_template('Accesinfopatient.html', charge=charge, charge2=charge2)
    
#    return render_template( 'usager.html',Patient=info_patient,   Medecin=info_medecin,   Organisation=info_organisation,Medication=Medication)





















# @app.route('/Register', methods=['POST'])
# def registre():
#     login = str(request.args.get('Id'))
#     mdp = request.args.get('Nom')
#     age=request.args.get('Age')
#     mail=request.args.get('Mail')
#     tel=request.args.get('Telephone')
    
#     if request.method == 'POST':
#         login = request.form['login']
#         mdp = request.form['mdp']
#         member={ "login": login, "mdp":mdp}
#         f = open('login_mdp.json','w')
#         data["member"].append(member)
#         json.dump(data,f)
#         f.close()
#         return render_template('Connecter.html', title='Connecter')


   


    
    
    # ident = str(request.args.get('Id'))
    # nom = request.args.get('Nom')
    # prenom=request.args.get('Prenom')
    # age=request.args.get('Age')
   
    # mail=request.args.get('Mail')
    # tel=request.args.get('Telephone')
    
    

    
    # fichier = "fhir/Patient/"+ ident +".json"
    # donne = {
    #   "resourceType" : "Patient",
    #   "Id":str(ident),
    #   "Nom" : str(nom),
    #   "Prenom" : str(prenom),
    #   "Date_Naissance" : str(age),
    #   "Mail": str(mail),
    #   "Telephone": str(tel),
    #   "organization" : "/fhir/Organization?_id="+ ident
    # }
    # with open(fichier, "w") as fichier_edite :
    #     json.dump(donne, fichier_edite, indent=2)
    # var = open(fichier)
    # charge = json.load(var)
    # var.close()

    # return render_template("InscriptionPatient.html", charge=charge)






# @app.route('/Register',methods=["POST"])

# def Register():
#     if request.method == 'POST':
     
            
#         login = request.form['login']
#         mdp = request.form['mdp']
#         member={ "login": login, "mdp":mdp}
#         f = open('login_mdp.json','w')
#         data["member"].append(member)
#         json.dump(data,f)
#         f.close()
#         return render_template('Connecter.html', title='Connecter')






# @app.route('/fhir/Patient/Connexion', methods=['GET'])
# def connexionPatient():
#     ident = str(request.args.get('Id'))
#     nom = request.args.get('Nom')
#     prenom=request.args.get('Prenom')
#     age=request.args.get('Age')
#     sexe=request.args.get('Sexe')
#     mail=request.args.get('Mail')
#     tel=request.args.get('Telephone')

    
#     fichier = "fhir/Patient/"+ ident +".json"
#     donne = {
#       "resourceType" : "Patient",
#       "Id":str(ident),
#       "Nom" : str(nom),
#       "Prenom" : str(prenom),
#       "Age" : str(age),
#       "Sexe": str(sexe),
#       "Mail": str(mail),
#       "Telephone": str(tel),
#       "organization" : "/fhir/Organization?_id="+ ident
#     }
#     with open(fichier, "w") as fichier_edite :
#         json.dump(donne, fichier_edite, indent=2)
#     var = open(fichier)
#     charge = json.load(var)
#     var.close()

#     return render_template("index.html", charge=charge)
# @app.route('/fhir/Patient', methods=['GET'])
# def patient():
#     ident = str(request.args.get('id'))
    
#     fichier = "fhir/Patient/"+ ident +".json"
#     var = open(fichier)
#     charge = json.load(var)
#     var.close()
    
#     fichier2 = "fhir/Immunization/"+ ident +".json"
#     var2 = open(fichier2)
#     charge2 = json.load(var2)
#     var2.close()
    
#     fichier3 = "fhir/Medicamment/"+ ident +".json"
#     var3 = open(fichier3)
#     charge3 = json.load(var3)
#     var3.close()    
#     return render_template("home.html",charge=charge, charge2=charge2, charge3=charge3)

    


    
# @app.route('/fhir/Pro', methods=['GET'])
# def pro():
#     ident = str(request.args.get('id'))
    
#     fichier = "fhir/Pro/"+ ident +".json"
#     var = open(fichier)
#     charge = json.load(var)
#     var.close()
    
#     fichier2 = "fhir/Immunization/"+ ident +".json"
#     var2 = open(fichier2)
#     charge2 = json.load(var2)
#     var2.close()
    
#     fichier3 = "fhir/Medicamment/"+ ident +".json"
#     var3 = open(fichier3)
#     charge3 = json.load(var3)
#     var3.close()    
#     return render_template("home.html",charge=charge, charge2=charge2, charge3=charge3)


@app.route('/chat')#, methods=['GET', 'POST'])
def ordonance():
    return render_template('chat.html')
    

@app.route('/RendezvousPatient')#, methods=['GET', 'POST'])
def rendezvousPatient():
    # sender_email="Santé_Live.episen.com"
    # password="vitrygtr"
    # MailPatient=(request.arg.get('MailPatient'))
    # DateHoraire=str(request.arg.get('DateHoraire'))
    
    
    # fichier = "fhir/Patient/"+str(MailPatient) +".json"
    # var = open(fichier)
    # charge= json.load(var)
    # var.close()
    
    # msg="Cher" + charge['Prenom'] + "" + charge['Nom'] +", \n\nVotre rendez-vous aura lieu le "+ DateHoraire + ". \n\nA bientient§ \n\nE_live_Santé"
    # if MailPatient!=None:
    #     server=smtplib.SMTP("smtp.gmail.com", 587)
    #     server.starttls()
    #     server.login(sender_email,password)
    #     server.sendermail(sender_email, MailPatient,msg)
    return render_template('RendezvousPatient.html')












if __name__ == '__main__':
    #app.run(debug=True)
    
    
    #app.run(ss1_context,host='192.168.1.64', port=5000)
    app.run(host='0.0.0.0', port=5000)
