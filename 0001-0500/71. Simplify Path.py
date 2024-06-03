class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for name in path:
            if name == '' or name == '.':
                continue
            elif name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(name)
        return '/' + '/'.join(stack)

  
