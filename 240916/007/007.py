class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

secrets = list(input().split())
secret1 = Secret(secrets[0], secrets[1], secrets[2])
print(f'secret code : {secret1.code}')
print(f'meeting point : {secret1.place}')
print(f'time : {secret1.time}')