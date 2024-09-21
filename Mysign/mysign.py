from django.core.signing import TimestampSigner
class myTimestampSigner(TimestampSigner):
    def sign(self,value):
        print(value)
        return value + 'Test'