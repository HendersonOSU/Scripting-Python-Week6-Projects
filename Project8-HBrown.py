
infile=input("enter the input filenam + extension ");


outfile=input("enter the output filename + extension ");


f1=open(infile,"r");


f2=open(outfile,"w+");


content=f1.read();


f2.write(content);

f1.close();
f2.close();
