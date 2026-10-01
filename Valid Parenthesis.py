class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []

        for i in range(len(s)):

            # print(i)

            if s[i] == "(" or s[i] == '{' or s[i] == '[':

                st.append(s[i])

            else:

                # print(st)

                if len(st) ==0:

                    return False

                val = st.pop()

                # print(val)

                # print(st)

                if s[i] == ")" and val!="(" or s[i] == "}" and  val != "{" or s[i] == "]" and  val != "[":

                    return False

            # print(len(st))

            # print(st)

        return len(st) == 0
