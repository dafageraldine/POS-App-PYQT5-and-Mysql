from flask import Flask, render_template, request, redirect, send_from_directory
import mysql.connector
import json
from Module.sql import *
import jinja2.ext


app = Flask(__name__, static_folder='static')

# Configure db
mydb = db('localhost', 'root', '12345678', 'bullEyeArchery')

@app.route('/api/pelanggan', methods=['GET'])
def index():
    id_pel = request.args.get('id')
    get_id = "idPelanggan=\"{}\""
    if id_pel is None:
        userDetails = mydb.selectAll("pelanggan", True)
        jsondata = json.dumps(userDetails)
    else :
        userDetails = mydb.findAll("pelanggan", get_id.format(id_pel),False)
        jsondata = json.dumps({ "idPelanggan" : userDetails[1], "rfid" : userDetails[2], "nama" : userDetails[3], "gender" : userDetails[4], "member" : userDetails[5], "alamat" : userDetails[6], "kontak" : userDetails[7], "foto_id" : userDetails[8], "saldo" : userDetails[9], "point" : userDetails[10] })
    return jsondata

@app.route('/api/pelanggan/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        # Fetch form data
        jsondata = request.get_json()
        idPelanggan = jsondata['idPelanggan']
        nama = jsondata['nama']
        gender = jsondata['gender']
        member = jsondata['member']
        alamat = jsondata['alamat']
        kontak = jsondata['kontak']
        foto = jsondata['foto']
        saldo = jsondata['saldo']
        point = jsondata['point']
        val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
        val = val.format(idPelanggan,nama,gender,member,alamat,kontak,foto,saldo,point)
        mydb.insertTo("pelanggan", "`idPelanggan`, `nama`, `gender`, `member`, `alamat`, `kontak`, `foto`, `saldo`, `point`", val)
        return redirect('/api/pelanggan')
    return redirect('/api/pelanggan')

@app.route('/api/pelanggan/update', methods=['POST'])
def update():
    jsondata = request.get_json()
    id = jsondata['id']
    idPelanggan = jsondata['idPelanggan']
    nama = jsondata['nama']
    alamat = jsondata['alamat']
    kontak = jsondata['kontak']
    get_id = "id=\"{}\""
    setValue = "idPelanggan = \"{}\", nama = \"{}\", alamat = \"{}\", kontak = \"{}\""
    mydb.update("pelanggan", setValue.format(idPelanggan,nama,alamat,kontak), get_id.format(id))
    return redirect('/api/pelanggan')

@app.route('/api/pelanggan/image', methods = ['GET'])
def imagehandler():
    img_data = request.args.get('img')
    filename = img_data +'.png'
    return send_from_directory('static',filename,mimetype='image/png')

@app.route('/api/ads', methods = ['GET'])
def adshandler():
    img_data = request.args.get('id')
    filename = img_data +'.png'
    return send_from_directory('static',filename,mimetype='image/png')

#if __name__ == '__main__':
#    app.run(host='',debug=True)
