#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()							//문자열 배열 동적 할당
{
	int N;
	scanf("%d", &N);

	char **names = (char **)malloc(sizeof(char *) * N);
	char buffer[51];	//50글자를 넘을수 없음.
	int len;


	for (int i = 0; i < N; i++)
	{
		scanf("%s", buffer);
		len = strlen(buffer);

		char *nbuffer = (char *)malloc((len + 1) * sizeof(char));
		strcpy(nbuffer, buffer);
		names[i] = nbuffer;
	}

	char *answer = (char *)malloc(sizeof(char) * len);

	for (int index = 0; index < len; index++)
	{
		char temp = names[0][index];
		int check=1;
		for (int i = 0; i < N; i++)
		{
			if (temp != names[i][index])
			{
				answer[index] = '?';
				check = 0;
				break;
			}
		}
		if(check) answer[index] = temp;
	}
	for (int i = 0; i < len; i++)
	{
		printf("%c", answer[i]);
	}
}