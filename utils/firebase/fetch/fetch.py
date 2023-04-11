import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def fetchFromFirebase(collection, document):
    # Use a service account.
    cred = credentials.Certificate('utils/firebase/secret/dsci2023-firebase-adminsdk-t47pf-555db158e8.json')

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()

    doc_ref = db.collection(u'%s'%(collection)).document(u'%s'%(document))

    doc = doc_ref.get().to_dict()

    return doc

#usage
# ans = fetchFromFirebase('your collection name', 'your document name')
#    ans= {
#         "new" : your array,
#         "old" : your array,
#     }

#     arr = ans['new']
#     arr = ans['old']

