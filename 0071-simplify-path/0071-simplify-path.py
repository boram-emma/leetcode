class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # double // to single /
        path = path.replace('//', '/')

        # end of input, remove single /
        if path[-1] == '/':
            path = path[:-1]
  
        # split path based on /- & remove /. when /./
        path_split = path.split('/')
        path_split = [p for p in path_split if p not in ('', '.')]

        stack = []
        for file_name in path_split:
            if file_name != '..':
                stack.append(file_name)
            else:
                if stack:
                    stack.pop()
        
        canonical_path = '/' + '/'.join(stack)

        return canonical_path


