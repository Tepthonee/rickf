FROM Tepthonee/rickf:slim-buster

 #clonning repo 
 RUN git clone https://github.com/Tepthonee/rickf /root/jepthon
 #working directory 
 WORKDIR /root/jepthon
 RUN apk add --update --no-cache p7zip
 # Install requirements
 RUN pip3 install --no-cache-dir -r requirements.txt
 ENV PATH="/home/jepthon/bin:$PATH"
 CMD ["python3","-m","jepthon"]
