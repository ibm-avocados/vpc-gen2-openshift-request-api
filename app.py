from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/ping',methods=['GET'])
def ping():
    return {"status": "pong"}


@app.route('/create',methods=['POST'])
def create():
    posted_data = request.json
    APIKEY=posted_data["APIKEY"]
    WORKSPACE=posted_data["WORKSPACE"]
    GHEKEY=posted_data["GHEKEY"]
    COUNTNUMBER=posted_data["COUNTNUMBER"]
    REGION=posted_data["REGION"]
    os.system("ibmcloud login --apikey {0} -r 'us-south'".format(APIKEY))
    os.system('ibmcloud target -g "Default"')
    os.system('ibmcloud ce project select -n grant-cluster')
    os.system("ibmcloud ce jobrun submit --job vpc-gen2-openshift -a {0} -a {1} -a {2} -a {3} -a {4}".format(APIKEY,WORKSPACE,GHEKEY,COUNTNUMBER,REGION))
    print("Running the command...")
    return jsonify(posted_data)

@app.route('/delete',methods=['DELETE'])
def delete():
    posted_data = request.json
    APIKEY=posted_data["APIKEY"]
    WORKSPACE=posted_data["WORKSPACE"]
    os.system("ibmcloud login --apikey {0} -r 'us-south'".format(APIKEY))
    os.system('ibmcloud target -g "Default"')
    os.system('ibmcloud plugin install schematics -f')
    os.system("ID_WORKSPACE=$(ibmcloud schematics workspace list | grep {0} | cut -d ' ' -f 4) && ibmcloud schematics destroy --id $ID_WORKSPACE -f ".format(WORKSPACE))
    print("Deleting a workspace...")
    return jsonify(posted_data)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')