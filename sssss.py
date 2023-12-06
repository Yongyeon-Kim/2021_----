import math

class DecisionTree2:
    class TreeNode:
        def __init__(self, entropy, value, name):
            self.entropy = entropy
            self.value = value
            self.name = name
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def get_data(self):
        self.x = {"body_shape":["타원", "타원", "사각형", "사각형", "사각형", "사각형", "사각형", "타원", "타원", "사각형", "타원", "타원"],
                  "body_color":["흰색", "회색", "흰색", "흰색", "흰색", "회색", "흰색", "흰색", "흰색", "흰색", "흰색", "흰색"],
                  "head_shape":["사각형", "원", "사각형", "사각형", "사각형",  "원", "사각형", "사각형", "사각형", "사각형", "사각형", "원"],
                  "class":["no", "yes", "yes", "yes", "yes", "no", "yes", "no", "no", "yes", "no", "yes"]}
        self.features = ["body_shape", "body_color", "head_shape"] # 자식 노드 저장
        self.target = "class"
        return

    def set_data(self):
        self.get_data()
        data_list = []
        for i in self.features:
            data  = self.x[i]                
            data_list.append(data)
        data_list.append(self.x[self.target])

        self.data_list = list(map(list, zip(*data_list)))
        print(self.data_list, '\n')

    def Target_Entropy(self, node):
        target = self.x[node]

        value = [0, 0]
        for i in target:
            if "yes" == i:
                value[0] += 1
            else:
                value[1] += 1
        Target_Entropy = self.Entropy(value) # 루트 노드 엔트로피 값 계산
        if Target_Entropy != 0:
            print("상위 노드의 엔트로피: {Entropy} 입니다.".format(Entropy=Target_Entropy), '\n')
        else:
            print("=========================================================================")
        
        return target, Target_Entropy

    def Entropy(self, cnt): # Entropy 계산 함수
        try:
            entropy = -(sum(cnt[i]/sum(cnt)*math.log2(cnt[i]/sum(cnt))for i in range(len(counts)))) # Entropy 계산 식
        except BaseException as e:
            if cnt[0] == 0 and cnt[1] == 0: entropy=0
            elif cnt[0] == 0: 
                entropy = -(cnt[1]/sum(cnt)*math.log2(cnt[1]/sum(cnt)))
            elif cnt[1] == 0:
                entropy = -(cnt[0]/sum(cnt)*math.log2(cnt[0]/sum(cnt)))

        return entropy # 결과 값 리턴

    def new_node(self, data, value, name):
        self.root = self.insert_node(self.root, data, value, name)

    def insert_node(self, node, data, value, name):
        if node is None:
            node = self.TreeNode(data, value, name)
            return node

        if data < node.data:
            node.left = self.insert_node(node.left, data, value, name)
        elif data > node.data:
            node.right = self.insert_node(node.right, data, value, name)
        return node

    def IG(self, x, target, Target_Entropy):
        feacture = self.x[x]
        feacture_uni = list(set(feacture))

        feacture_cnt = [0,0]
        target_cnt = [[0,0],[0,0]]
        for f in range(len(feacture)):
            if feacture_uni[0] == feacture[f]:
                feacture_cnt[0] += 1
                if "yes" == target[f]:
                    target_cnt[0][0] += 1
                else:
                    target_cnt[0][1] += 1
            else:
                feacture_cnt[1] += 1
                if "yes" == target[f]:
                    target_cnt[1][0] += 1
                else:
                    target_cnt[1][1] += 1

        Weighted_Entropy1 = feacture_cnt[0]/sum(feacture_cnt) * self.Entropy(target_cnt[0]) # 각 속성의 엔트로피
        Weighted_Entropy2 = feacture_cnt[1]/sum(feacture_cnt) * self.Entropy(target_cnt[1]) # 각 속성의 엔트로피
        Feacture_Entropy = Weighted_Entropy1 + Weighted_Entropy2
        print('E(', x, ') = ', round(Feacture_Entropy, 5)) # 출력

        Information_Gain = Target_Entropy - Feacture_Entropy # ig값 계산
        value = [ target_cnt[0][0]+ target_cnt[1][0], target_cnt[0][1]+ target_cnt[1][1]]
        return Information_Gain

    def split(self, index, node):
        feacture = self.x[node]  # 해당 열의 데이터 추출
        feacture_unique = list(set(feacture))
        name_1 = feacture_unique[0]; name_2 = feacture_unique[1]
        name_1_list = []; name_2_list = []; 

        for i in self.data_list:
            if i[index] == name_1:
                name_1_list.append(i)
            elif i[index] == name_2:
                name_2_list.append(i)
        
        new_list = list(map(list, zip(*name_1_list)))
        for i in range(len(new_list)):
            if i==0:
                self.x['body_shape'] = new_list[i]
            elif i==1:
                self.x['body_color'] = new_list[i]
            elif i==2:
                self.x['head_shape'] = new_list[i]
            elif i==3:
                self.x['class'] = new_list[i]
        self.doMain()

        new_list = list(map(list, zip(*name_2_list)))
        for i in range(len(new_list)):
            if i==0:
                self.x['body_shape'] = new_list[i]
            elif i==1:
                self.x['body_color'] = new_list[i]
            elif i==2:
                self.x['head_shape'] = new_list[i]
            elif i==3:
                self.x['class'] = new_list[i]
        self.doMain()

    def doMain(self):
        self.set_data()
        target, Target_Entropy = self.Target_Entropy(self.target)

        if Target_Entropy != 0:
            IG_result = []
            for x in self.features: # 자식 노드 x로 순차 반환
                ig = self.IG(x, target, Target_Entropy)
                print('InfoGain(' + x +') = ', ig, '\n') # 자식노드와 부모노드 IG()로 호출하여 전달, 결과 출력
                IG_result.append(ig)

            max_index = IG_result.index(max(IG_result))
            node = self.features[max_index]
            print("InfoGain이 최대가 되는 분기조건: ", node, '\n')
            
            index = self.features.index(node)
            self.split(index, node)
        else:
            return


DT = DecisionTree2()
DT.doMain()