import jwt
#encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
#print(encoded)
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U
#jwt.decode(encoded, "secret", algorithms=["HS256"])
#{'some': 'payload'}

def create_jwt_toke(payload,key,algo):
    return jwt.encode(payload, key,algorithm=algo)

def decode_jwt_token(token,key,algo):
    return jwt.decode(token,key,algorithm=algo)