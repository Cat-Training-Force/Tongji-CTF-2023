flag = b"tjctf{...}..."

e = 191
p = 115454544015599150711525810879125485218158876863413904525004934220198757859356085118059908709057748261520507430434023140065098340351050254870943914108718470257154791297820228452801441913937900764632352422262383423576663832008718427558738772403390021363437566445995301950866790685622330139500896451192078274361
q = 172853206455421729776180172751124644903134249913948790535966034315036074203854054164604507127234846800687352458891000089040513423939825098230608319961771162233020977760025275862967322672515780852490807580220838608760264350985887420688113146642443706792083281947667852108402345005017868730472869424870810770009
n = p * q
m = int.from_bytes(flag, "big")
c = pow(m, e, n)
print(f"c = {c}")

# c = 12646592790423069519341938615596855421416703595148612718022653323835082504544015923979719972644156519411044019479636690130904951849657286502686420912244741095492469499965995807933039401031713231293442081841384659908306144564268511659578662953252944570445950524454994515003739027184305930115576863935883670382673195966427559925822121344492313929626370023688972539799073482455006499780839720147906778213045103897944370718358440113317560277780776480479819493361673681439127592815525150756421200412002564503777444656420795380861453783145833155492850259336528456066093505531629534879789897293936698127626079777535814243476
