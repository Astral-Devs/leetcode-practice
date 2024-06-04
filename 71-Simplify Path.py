def simplifyPath(self, path: str) -> str:
        locations = path.split('/')
        stack = []
        for loc in locations:
            if loc == '' or loc == '.':
                continue          
            if loc == '..' and stack:
                stack.pop()
            elif loc not in '..':
                stack.append(loc)

        return "/" + "/".join(stack)
