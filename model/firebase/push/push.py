import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def pushToFirebase(data, collection, document, objectName):
    # Use a service account.
    cred = credentials.Certificate('../secret/dsci2023-firebase-adminsdk-t47pf-555db158e8.json')

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()

    if objectName.length == 1:
        obj = {
            f'{objectName[0]}': data,
            }
    else:
        obj = {
            f'{objectName[0]}': data[0],
            f'{objectName[1]}': data[1],
        }

    db_ref = db.collection(u'%s'%(collection)).document(u'%s'%(document)).set(obj)
