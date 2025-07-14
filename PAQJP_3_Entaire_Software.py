g='%0*x'
Y='rb'
X='wb'
W=input
V=bin
U=True
T=False
S='utf-8'
P=ValueError
N=Exception
M=open
L=print
J='1'
I='0'
H=''
G=int
F=bytes
E=bytearray
D=None
C=range
A=len
import os,sys,math as Z,struct,array,random as K,heapq as Q,binascii as O,logging as B,paq,zlib as R
from datetime import datetime as a
from typing import List,Dict,Tuple,Optional,Union
from enum import Enum as b
B.basicConfig(level=B.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
s='PAQJP_3'
h=9
t=65536<<h
i=1024
c=[A for A in C(2,256)if all(A%B!=0 for B in C(2,G(A**.5)+1))]
class u(b):DEFAULT=0;JPEG=1;EXE=2;TEXT=3
class v(b):COMPRESS=0;DECOMPRESS=1
class w:
	def __init__(A,s=H):A.data=E(s.encode(S))
	def resize(B,new_size):
		C=new_size
		if C>A(B.data):B.data+=E(C-A(B.data))
		else:B.data=B.data[:C]
	def size(B):return A(B.data)
	def c_str(A):return A.data.decode(S)
	def __iadd__(A,s):A.data+=s.encode(S);return A
	def __getitem__(A,index):return A.data[index]
	def __setitem__(A,index,value):A.data[index]=value
	def __str__(A):return A.data.decode(S)
class d:
	def __init__(A,size=0,initial_value=0):A.data=array.array('B',[initial_value]*size)
	def resize(B,new_size):
		C=new_size
		if C>A(B.data):B.data.extend([0]*(C-A(B.data)))
		else:B.data=B.data[:C]
	def size(B):return A(B.data)
	def __getitem__(A,index):return A.data[index]
	def __setitem__(A,index,value):A.data[index]=value
	def __len__(B):return A(B.data)
class j:
	def __init__(A,size=0):A.size_=size;A.data=d(size);A.pos=0
	def setsize(B,size):
		A=size
		if A>0 and A&A-1==0:B.size_=A;B.data.resize(A)
	def __getitem__(A,index):return A.data[index&A.size_-1]
	def __call__(A,i):return A.data[A.pos-i&A.size_-1]
	def size(A):return A.size_
x=j()
class e:
	def __init__(A,left=D,right=D,symbol=D):A.left=left;A.right=right;A.symbol=symbol
	def is_leaf(A):return A.left is D and A.right is D
class k:
	def __init__(A):A.table=[[1,2,0,0],[3,5,1,0],[4,6,0,1],[7,10,2,0],[8,12,1,1],[9,13,1,1],[11,14,0,2],[15,19,3,0],[16,23,2,1],[17,24,2,1],[18,25,2,1],[20,27,1,2],[21,28,1,2],[22,29,1,2],[26,30,0,3],[31,33,4,0],[32,35,3,1],[32,35,3,1],[32,35,3,1],[32,35,3,1],[34,37,2,2],[34,37,2,2],[34,37,2,2],[34,37,2,2],[34,37,2,2],[34,37,2,2],[36,39,1,3],[36,39,1,3],[36,39,1,3],[36,39,1,3],[38,40,0,4],[41,43,5,0],[42,45,4,1],[42,45,4,1],[44,47,3,2],[44,47,3,2],[46,49,2,3],[46,49,2,3],[48,51,1,4],[48,51,1,4],[50,52,0,5],[53,43,6,0],[54,57,5,1],[54,57,5,1],[56,59,4,2],[56,59,4,2],[58,61,3,3],[58,61,3,3],[60,63,2,4],[60,63,2,4],[62,65,1,5],[62,65,1,5],[50,66,0,6],[67,55,7,0],[68,57,6,1],[68,57,6,1],[70,73,5,2],[70,73,5,2],[72,75,4,3],[72,75,4,3],[74,77,3,4],[74,77,3,4],[76,79,2,5],[76,79,2,5],[62,81,1,6],[62,81,1,6],[64,82,0,7],[83,69,8,0],[84,76,7,1],[84,76,7,1],[86,73,6,2],[86,73,6,2],[44,59,5,3],[44,59,5,3],[58,61,4,4],[58,61,4,4],[60,49,3,5],[60,49,3,5],[76,89,2,6],[76,89,2,6],[78,91,1,7],[78,91,1,7],[80,92,0,8],[93,69,9,0],[94,87,8,1],[94,87,8,1],[96,45,7,2],[96,45,7,2],[48,99,2,7],[48,99,2,7],[88,101,1,8],[88,101,1,8],[80,102,0,9],[103,69,10,0],[104,87,9,1],[104,87,9,1],[106,57,8,2],[106,57,8,2],[62,109,2,8],[62,109,2,8],[88,111,1,9],[88,111,1,9],[80,112,0,10],[113,85,11,0],[114,87,10,1],[114,87,10,1],[116,57,9,2],[116,57,9,2],[62,119,2,9],[62,119,2,9],[88,121,1,10],[88,121,1,10],[90,122,0,11],[123,85,12,0],[124,97,11,1],[124,97,11,1],[126,57,10,2],[126,57,10,2],[62,129,2,10],[62,129,2,10],[98,131,1,11],[98,131,1,11],[90,132,0,12],[133,85,13,0],[134,97,12,1],[134,97,12,1],[136,57,11,2],[136,57,11,2],[62,139,2,11],[62,139,2,11],[98,141,1,12],[98,141,1,12],[90,142,0,13],[143,95,14,0],[144,97,13,1],[144,97,13,1],[68,57,12,2],[68,57,12,2],[62,81,2,12],[62,81,2,12],[98,147,1,13],[98,147,1,13],[100,148,0,14],[149,95,15,0],[150,107,14,1],[150,107,14,1],[108,151,1,14],[108,151,1,14],[100,152,0,15],[153,95,16,0],[154,107,15,1],[108,155,1,15],[100,156,0,16],[157,95,17,0],[158,107,16,1],[108,159,1,16],[100,160,0,17],[161,105,18,0],[162,107,17,1],[108,163,1,17],[110,164,0,18],[165,105,19,0],[166,117,18,1],[118,167,1,18],[110,168,0,12],[169,105,20,0],[170,117,19,1],[118,171,1,19],[110,172,0,20],[173,105,21,0],[174,117,20,1],[118,175,1,20],[110,176,0,21],[177,105,22,0],[178,117,21,1],[118,179,1,21],[110,180,0,22],[181,115,23,0],[182,117,22,1],[118,183,1,22],[120,184,0,23],[185,115,24,0],[186,127,23,1],[128,187,1,23],[120,188,0,24],[189,115,25,0],[190,127,24,1],[128,191,1,24],[120,192,0,25],[193,115,26,0],[194,127,25,1],[128,195,1,25],[120,196,0,26],[197,115,27,0],[198,127,26,1],[128,199,1,26],[120,200,0,27],[201,115,28,0],[202,127,27,1],[128,203,1,27],[120,204,0,28],[205,115,29,0],[206,127,28,1],[128,207,1,28],[120,208,0,29],[209,125,30,0],[210,127,29,1],[128,211,1,29],[130,212,0,30],[213,125,31,0],[214,137,30,1],[138,215,1,30],[130,216,0,31],[217,125,32,0],[218,137,31,1],[138,219,1,31],[130,220,0,32],[221,125,33,0],[222,137,32,1],[138,223,1,32],[130,224,0,33],[225,125,34,0],[226,137,33,1],[138,227,1,33],[130,228,0,34],[229,125,35,0],[230,137,34,1],[138,231,1,34],[130,232,0,35],[233,125,36,0],[234,137,35,1],[138,235,1,35],[130,236,0,36],[237,125,37,0],[238,137,36,1],[138,239,1,36],[130,240,0,37],[241,125,38,0],[242,137,37,1],[138,243,1,37],[130,244,0,38],[245,135,39,0],[246,137,38,1],[138,247,1,38],[140,248,0,39],[249,135,40,0],[250,69,39,1],[80,251,1,39],[140,252,0,40],[249,135,41,0],[250,69,40,1],[80,251,1,40],[140,252,0,41]]
	def nex(A,state,sel):return A.table[state][sel]
y=k()
def l(dt=D):
	C=dt
	if C is D:C=a.now()
	H=C.second;I=C.minute;J=C.hour;K=C.weekday();L=C.month;M=C.day;G=C.year
	if not(0<=H<=59 and 0<=I<=59 and 0<=J<=23 and 0<=K<=6 and 1<=L<=12 and 1<=M<=31 and 0<=G<=4095):B.error('Invalid date/time values for encoding');raise P('Date/time values out of range')
	A=E();A.append(H);A.append(I);A.append(J);A.append(K);A.append(L);A.append(M);A.append(G//256);A.append(G%256);A.append(0);return F(A)
def m(data):
	K='Decoded date/time values out of range';C=data
	if A(C)<9:B.error('Insufficient data for datetime decoding');raise P('Data too short for datetime decoding')
	D=C[0];E=C[1];F=C[2];G=C[3];H=C[4];I=C[5];J=C[6]<<8|C[7];L=C[8]
	if not(0<=D<=59 and 0<=E<=59 and 0<=F<=23 and 0<=G<=6 and 1<=H<=12 and 1<=I<=31 and 0<=J<=4095 and L==0):B.error(K);raise P(K)
	return D,E,F,G,H,I,J
def n(data,repeat=1000):
	G=repeat;B=E(data)
	for D in c:
		H=D if D==2 else max(1,Z.ceil(D/2/G))
		for J in C(G):
			for I in C(0,A(B),3):B[I]^=H
	return F(B)
def o(data,chunk_size=4):
	B=chunk_size;D=E()
	for G in C(0,A(data),B):H=data[G:G+B];D.extend([A^255 for A in H])
	return F(D)
def f(n):
	if n<2:return T
	if n==2:return U
	if n%2==0:return T
	for A in C(3,G(n**.5)+1,2):
		if n%A==0:return T
	return U
def z(n):
	A=0
	while U:
		if f(n-A):return n-A
		if f(n+A):return n+A
		A+=1
def quit(message=D):
	A=message
	if A:L(A)
	sys.exit(1)
def A0(x):
	if x<0:return 0
	A=0
	while x>0:x>>=1;A+=1
	return A
def q(d,n=12,repeat=1000):
	B=(1<<n)-1;A=d
	for E in C(repeat):
		if A>2047:A=B
		if A<-2047:A=0
		D=(1<<n)/(1+Z.exp(-A/512.));A=G(D);A=min(max(A,0),B)
	return A
def A1(p):
	A=d(4096);B=0
	for D in C(-2047,2048):
		E=q(D)
		for F in C(B,E+1):A[F]=D
		B=E+1
	A[4095]=2047;return A[p]
def hash(*B):C=B[0]*200002979+B[1]*30005491+(B[2]if A(B)>2 else 4294967295)*50004239+(B[3]if A(B)>3 else 4294967295)*70004807+(B[4]if A(B)>4 else 4294967295)*110002499;return C^C>>9^B[0]>>2^B[1]>>3^(B[2]if A(B)>2 else 0)>>4^(B[3]if A(B)>3 else 0)>>5^(B[4]if A(B)>4 else 0)>>6
class p:
	def __init__(A):A.compressor=D;A.PRIMES=c;A.seed_tables=A.generate_seed_tables();A.max_intersections=28
	def generate_seed_tables(D,num_tables=126,table_size=256,min_val=5,max_val=255,seed=42):
		K.seed(seed);A=[]
		for E in C(num_tables):B=[K.randint(min_val,max_val)for A in C(table_size)];A.append(B)
		return A
	def get_seed(B,table_idx,value):
		C=table_idx
		if 0<=C<A(B.seed_tables):return B.seed_tables[C][value%A(B.seed_tables[C])]
		return 0
	def binary_to_file(L,binary_data,filename):
		D=binary_data
		try:
			E=G(D,2);F=(A(D)+7)//8;C=g%(F*2,E)
			if A(C)%2!=0:C=I+C
			H=O.unhexlify(C)
			with M(filename,X)as J:J.write(H)
			return U
		except N as K:B.error(f"Error saving file: {str(K)}");return T
	def file_to_binary(H,filename):
		try:
			with M(filename,Y)as D:
				C=D.read()
				if not C:B.error('Error: Empty file');return
				E=V(G(O.hexlify(C),16))[2:];return E.zfill(A(C)*8)
		except N as F:B.error(f"Error reading file: {str(F)}");return
	def calculate_frequencies(C,binary_str):
		A={}
		for B in binary_str:A[B]=A.get(B,0)+1
		return A
	def build_huffman_tree(H,frequencies):
		B=[(B,e(symbol=A))for(A,B)in frequencies.items()];Q.heapify(B)
		while A(B)>1:C,D=Q.heappop(B);E,F=Q.heappop(B);G=e(left=D,right=F);Q.heappush(B,(C+E,G))
		return B[0][1]
	def generate_huffman_codes(D,root,current_code=H,codes={}):
		C=current_code;B=codes;A=root
		if A.is_leaf():B[A.symbol]=C or I;return B
		if A.left:D.generate_huffman_codes(A.left,C+I,B)
		if A.right:D.generate_huffman_codes(A.right,C+J,B)
		return B
	def compress_data_huffman(B,binary_str):
		C=binary_str
		if not C:return H
		D=B.calculate_frequencies(C);E=B.build_huffman_tree(D);A=B.generate_huffman_codes(E)
		if I not in A:A[I]=I
		if J not in A:A[J]=J
		F=H.join(A[B]for B in C);return F
	def decompress_data_huffman(B,compressed_str):
		C=compressed_str
		if not C:return H
		F=B.calculate_frequencies(C);G=B.build_huffman_tree(F);I=B.generate_huffman_codes(G);D={B:A for(A,B)in I.items()};E=H;A=H
		for J in C:
			A+=J
			if A in D:E+=D[A];A=H
		return E
	def compress_data_zlib(C,data_bytes):
		try:return R.compress(data_bytes)
		except R.error as A:B.error(f"zlib compression error: {A}");return
	def decompress_data_zlib(C,compressed_data):
		try:return R.decompress(compressed_data)
		except R.error as A:B.error(f"zlib decompression error: {A}");return
	def transform_01(A,data):return n(data,repeat=1000)
	def reverse_transform_01(A,data):return A.transform_01(data)
	def transform_03(A,data):return o(data)
	def reverse_transform_03(A,data):return A.transform_03(data)
	def transform_04(G,data,repeat=50):
		B=E(data)
		for H in C(repeat):
			for D in C(A(B)):B[D]=(B[D]-D%256)%256
		return F(B)
	def reverse_transform_04(G,data,repeat=50):
		B=E(data)
		for H in C(repeat):
			for D in C(A(B)):B[D]=(B[D]+D%256)%256
		return F(B)
	def transform_05(H,data,shift=3):
		G=shift;B=E(data)
		for D in C(A(B)):B[D]=(B[D]<<G|B[D]>>8-G)&255
		return F(B)
	def reverse_transform_05(H,data,shift=3):
		G=shift;B=E(data)
		for D in C(A(B)):B[D]=(B[D]>>G|B[D]<<8-G)&255
		return F(B)
	def transform_06(H,data,seed=42):
		K.seed(seed);D=list(C(256));K.shuffle(D);B=E(data)
		for G in C(A(B)):B[G]=D[B[G]]
		return F(B)
	def reverse_transform_06(J,data,seed=42):
		K.seed(seed);G=list(C(256));K.shuffle(G);H=[0]*256
		for(B,I)in enumerate(G):H[I]=B
		D=E(data)
		for B in C(A(D)):D[B]=H[D[B]]
		return F(D)
	def paq_compress(A,data):return paq.compress(data)
	def paq_decompress(A,data):return paq.decompress(data)
	def compress_with_best_method(C,data):
		E=data;T=a(2025,7,14,13,56,0);U=l(T);W=[(1,C.transform_04),(2,C.transform_01),(3,C.transform_03),(5,C.transform_05),(6,C.transform_06)];X=[('paq',C.paq_compress),('zlib',C.compress_data_zlib)];H=D;I=float('inf');J=D;K=D
		for(P,Y)in W:
			Z=Y(E)
			for(Q,b)in X:
				try:
					L=b(Z)
					if L is D:continue
					R=A(L)
					if R<I:I=R;H=L;J=P;K=Q
				except N as c:B.warning(f"Compression method {Q} with transform {P} failed: {c}");continue
		if A(E)<i:
			d=V(G(O.hexlify(E),16))[2:].zfill(A(E)*8);S=C.compress_data_huffman(d);M=G(S,2).to_bytes((A(S)+7)//8,'big')
			if A(M)<I:I=A(M);H=M;J=4;K='huffman'
		if H is D:B.error('All compression methods failed.');return
		B.info(f"Best compression method: {K}, Marker: {J}");return F([J])+U+H
	def decompress_with_best_method(C,data):
		J=data;H=b''
		if A(J)<10:B.error('Empty or insufficient compressed data.');return H
		E=J[0];S=J[1:10];K=J[10:]
		try:T,U,W,X,Y,Z,a=m(S);B.info(f"Decoded datetime: {a}-{Y:02d}-{Z:02d} {W:02d}:{U:02d}:{T:02d}, Day of week: {X}")
		except P as F:B.error(f"Datetime decoding failed: {F}");return H
		Q={1:C.reverse_transform_04,2:C.reverse_transform_01,3:C.reverse_transform_03,5:C.reverse_transform_05,6:C.reverse_transform_06}
		if E==4:
			b=V(G(O.hexlify(K),16))[2:].zfill(A(K)*8);R=C.decompress_data_huffman(b)
			if not R:B.error('Huffman decompression failed.');return H
			try:
				c=(A(R)+7)//8;L=g%(c*2,G(R,2))
				if A(L)%2!=0:L=I+L
				return O.unhexlify(L)
			except N as F:B.error(f"Error converting decompressed Huffman data: {F}");return H
		if E not in Q:B.error(f"Unknown compression method marker: {E}");raise P(f"Unknown compression method marker: {E}")
		try:M=C.paq_decompress(K);return Q[E](M)
		except N as F:B.warning(f"PAQ decompression failed: {F}. Trying zlib...")
		M=C.decompress_data_zlib(K)
		if M is D:B.error('All decompression methods failed.');return H
		return Q[E](M)
def r():
	L('PAQJP_3 Compression System');L('Created by Jurijus Pacalovas.');L('Options:');L('1 - Compress file (PAQJP_3 with transformations and datetime)');L('2 - Decompress file (PAQJP_3 with transformations and datetime)');Q=p()
	try:
		G=W('Enter 1 or 2: ').strip()
		if G not in(J,'2'):B.error('Invalid choice. Exiting.');return
	except EOFError:B.info('No input detected. Defaulting to Compress (1).');G=J
	C=W('Input file name: ').strip();E=W('Output file name: ').strip()
	if not os.path.isfile(C):B.error(f"Error: Input file '{C}' does not exist.");return
	if G==J:
		with M(C,Y)as H:I=H.read()
		K=Q.compress_with_best_method(I)
		if K is D:return
		with M(E,X)as O:O.write(K)
		P=os.path.getsize(C);F=A(K);R=F/P*100 if P>0 else 0;B.info(f"Compression successful. Output saved to {E}. Size: {F} bytes");B.info(f"Original: {P} bytes, Compressed: {F} bytes, Ratio: {R:.2f}%")
	elif G=='2':
		with M(C,Y)as H:I=H.read()
		try:
			S=Q.decompress_with_best_method(I)
			with M(E,X)as O:O.write(S)
			F=os.path.getsize(C);T=os.path.getsize(E);B.info(f"Decompression successful. Output saved to {E}.");B.info(f"Compressed: {F} bytes, Decompressed: {T} bytes")
		except N as U:B.error(f"Error during decompression: {U}")
if __name__=='__main__':r()
