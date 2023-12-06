class Text:       
    def run_length(self, string):
        w = string.lower()
        result = ""
        count = 1
        for i in range(1, len(w)):
            if w[i] == w[i-1]:
                count +=1
            else:
                result += str(count) + w[i-1]
                count = 1
    
            if i == len(w)-1:
                result += str(count) + w[i]
                print("압축된 문자열: ",result)

string = input("문자열을 입력하시오: ")
t = Text()
t.run_length(string)

