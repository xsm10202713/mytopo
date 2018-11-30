//#include <config.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <memory.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*
 * Author:Liujia 2015/12/30
 * Description:
 * 	argv[1]存储的是ip地址最后8位的值，前面统一为10.0.0.
 * 	先创建并分别初始化本机地址my_addr, 目的主机地址dst_addr
 * 	创建套接字
 * 	绑定端口
 * 	发送数据包
 */
int main(int argc, char** argv)
{
 	///必须有目的ip的参数
	if(argc != 4)
	{
		printf("usage: send [ip] [number] [time interval(ms)]\n");
		return -1;
	}
	///根据参数组合出目的主机的ip地址
	char dst_ip[20];
	sprintf(dst_ip,"%s",argv[1]);
    int times = atoi(argv[2]);
    int time_interval = atoi(argv[3]);
    time_interval*=1000;
	/// 初始化本机地址
	struct sockaddr_in my_addr;
	memset(&my_addr,0,sizeof(my_addr));
	my_addr.sin_family = AF_INET; //Address family 指定为ipv4
	my_addr.sin_addr.s_addr = INADDR_ANY; ////INADDR_ANY表示自动获取本机地址
	my_addr.sin_port = htons(8889); ///端口号（本机的端口好表示用于发送的端口号）

	///初始化目的主机地址
	struct sockaddr_in dst_addr;
	memset(&dst_addr,0,sizeof(dst_addr));
	dst_addr.sin_family = AF_INET;
	dst_addr.sin_addr.s_addr = inet_addr(dst_ip);
	dst_addr.sin_port = htons(8888);

	///创建套接字
	int sockfd  =  socket(AF_INET,SOCK_DGRAM,0);
	if(sockfd == -1)
	{
		perror("create socket failed\n");
		return -1;
	}

	///绑定端口
	if(bind(sockfd,(struct sockaddr*)&my_addr,sizeof(my_addr)) == -1)
	{
		perror("bind failed\n");
		return -1;
	}

	unsigned char buf[16];
	int i = 0;
	for(i=0; i< 16; i++)
	{
		buf[i] = 0xff;
	}
	///发送数据包
    for(i=0; i<times; i++)
    {
        usleep(time_interval);
//        sleep(1);
        printf("sending packet %d to %s\n",i,dst_ip);
	    if(sendto(sockfd,buf,sizeof(buf),0,(struct sockaddr*)&dst_addr,sizeof(dst_addr)) == -1)
	    {
	    	perror("send failed\n");
	    	return -1;
	    }
    }
    close(sockfd);
}
