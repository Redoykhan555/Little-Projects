#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <math.h>
#define N 50000

uint32_t offset,size,width,height,compType;
uint16_t bpp;

unsigned char blue[N],green[N],red[N],wr;
double bl[N],gr[N],re[N];

struct Pixel{
	unsigned char r,g,b;
};

void dft(int total){
	int k,n;
	for(k=0;k<total;k++){
		bl[k] = 0;
		for(n=0;n<total;n++){
			bl[k] = bl[k]+(blue[n]*cos(M_PI/total*(n+.5)*k));
		}
		if(k%1000==0) printf("ok\n");
	}
}

void fft(){}

int main()
{
	unsigned char header[54];
	unsigned char buffer[N*3],image[N*3];
	FILE *fp;
	int i=0,j=0;
	fp=fopen("VENUS.BMP","rb");
	fread(header,54,1,fp);
	rewind(fp);
	if(fp==NULL)
	{
		printf("Can't read image\n");
		return 0;
	}
	void* x;
	fread(buffer,10,1,fp);
	
	fread(&offset,sizeof(offset),1,fp);
	fread(&size,sizeof(size),1,fp);
	fread(&width,sizeof(width),1,fp);
	fread(&height,sizeof(height),1,fp);
	fread(buffer,2,1,fp);
	fread(&bpp,sizeof(bpp),1,fp);
	fread(&compType,sizeof(compType),1,fp);
	printf("%d %d %d\n",(int)width,(int)height,(int)bpp);
	fread(buffer,20,1,fp);

	int total = height*width;
	
	fread(buffer,total*3,1,fp);
	fclose(fp);
	printf("Total:%d\n",total );
	
	struct Pixel *p;
	p = buffer;

	for(i=0;i<total;i++){
		blue[i] = p->b;
		green[i] = p->g;
		red[i] = p->r;
		p++;
	}
	printf("Data read\n");
	dft(total);
	printf("transformed\n");

	double t;
	double err = 0;
	int n,k;
	for(n=0;n<total;n++){
		t = 0;
		for(k=0;k<total;k++){
			t = t + (bl[k]*cos(M_PI/total*(n+.5)*k));
		}
		t = t/total;
		err+=t;
	}
	printf("reverse transformed\n");
	err = err/total;
	printf("error is : %lf\n",err);
	printf("Read data\n" );
	/*FILE* fw = fopen("test.bmp","wb");
	fwrite(header,54,1,fw);
	fwrite(buffer,total*3,1,fw);
	printf("written data\n" );
	*/
	return 0;
}
//
//
//