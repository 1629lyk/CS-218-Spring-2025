import sys
import collections
sys.setrecursionlimit(10**7)

def parse_pattern(p):
    """
    Parse p into a list of tokens of the form
      (typ, value, starred)
    where typ ∈ {'char','any','set','group'},
    value is either a character, None, a set of chars,
    or a sub‐list of tokens (for 'group'),
    and starred==True iff followed by '*'.
    """
    def _parse(i, end_char):
        tokens = []
        while i < len(p):
            ch = p[i]
            if end_char and ch == end_char:
                break
            if ch == '(':
                # parse inside parentheses up to ')'
                inner, j = _parse(i+1, ')')
                # j is index of ')'
                starred = (j+1 < len(p) and p[j+1] == '*')
                tokens.append(('group', inner, starred))
                i = j+2 if starred else j+1
            elif ch == '[':
                k = p.find(']', i+1)
                charset = set(p[i+1:k])
                starred = (k+1 < len(p) and p[k+1] == '*')
                tokens.append(('set', charset, starred))
                i = k+2 if starred else k+1
            elif ch == '?':
                starred = (i+1 < len(p) and p[i+1] == '*')
                tokens.append(('any', None, starred))
                i += 2 if starred else 1
            else:
                # a–z
                starred = (i+1 < len(p) and p[i+1] == '*')
                tokens.append(('char', ch, starred))
                i += 2 if starred else 1
        return tokens, i
    toks, _ = _parse(0, None)
    return toks

def build_nfa(tokens):
    """
    Build an NFA from the token list via Thompson's construction.
    Returns:
      eps_list   : list of lists, eps_list[u] = states reachable by ε from u
      trans_list : list of lists, trans_list[u] = [(v,cond_set),...]
      start, accept, num_states
    """
    eps = collections.defaultdict(list)
    trans = collections.defaultdict(list)
    next_state = 0

    def new_state():
        nonlocal next_state
        s = next_state
        next_state += 1
        return s

    def build_atom(typ, val):
        s = new_state()
        e = new_state()
        if typ == 'char':
            cond = {val}
        elif typ == 'any':
            cond = {chr(ord('a')+i) for i in range(26)}
        else:  # 'set'
            cond = val
        trans[s].append((e, cond))
        return (s, e)

    def concat(f1, f2):
        s1, e1 = f1
        s2, e2 = f2
        eps[e1].append(s2)
        return (s1, e2)

    def star(f):
        s1, e1 = f
        s = new_state()
        e = new_state()
        eps[s].append(s1)
        eps[s].append(e)
        eps[e1].append(s1)
        eps[e1].append(e)
        return (s, e)

    def build_frag(toks):
        frag = None
        for typ, val, starred in toks:
            if typ in ('char', 'any', 'set'):
                f = build_atom(typ, val)
            else:  # 'group'
                f = build_frag(val)
            if starred:
                f = star(f)
            if frag is None:
                frag = f
            else:
                frag = concat(frag, f)
        # empty pattern (shouldn't happen given constraints, but for safety)
        if frag is None:
            s = new_state(); e = new_state()
            eps[s].append(e)
            frag = (s, e)
        return frag

    start, accept = build_frag(tokens)
    N = next_state
    eps_list = [[] for _ in range(N)]
    for u, outs in eps.items():
        eps_list[u] = outs
    trans_list = [[] for _ in range(N)]
    for u, outs in trans.items():
        trans_list[u] = outs

    return eps_list, trans_list, start, accept, N

def compute_closure(eps_list, N):
    """
    For each state u, compute the ε-closure as a list.
    closure[u] = all states reachable from u by ε-moves.
    """
    closure = [None]*N
    for u in range(N):
        vis = [False]*N
        stack = [u]
        vis[u] = True
        while stack:
            x = stack.pop()
            for v in eps_list[x]:
                if not vis[v]:
                    vis[v] = True
                    stack.append(v)
        closure[u] = [i for i in range(N) if vis[i]]
    return closure

def solve():
    input = sys.stdin.readline
    t = int(input())
    NEG_INF = -10**9

    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        _m = int(input().strip())
        p = input().strip()

        # 1) Parse → tokens
        tokens = parse_pattern(p)
        # 2) Build NFA
        eps_list, trans_list, start, accept, N = build_nfa(tokens)
        # 3) Precompute ε-closures
        closure = compute_closure(eps_list, N)

        # 4) DP over the string s
        dp = [NEG_INF]*N
        # initialize: can be at any state in ε-closure(start) with length 0
        for u in closure[start]:
            dp[u] = 0

        for ch in s:
            dp_next = [NEG_INF]*N
            # try skip or match
            for u in range(N):
                if dp[u] < 0:
                    continue
                v0 = dp[u]
                # skip
                if v0 > dp_next[u]:
                    dp_next[u] = v0
                # match via any labeled edge
                for v, cond in trans_list[u]:
                    if ch in cond:
                        nv = v0 + 1
                        # enter ε-closure(v)
                        for w in closure[v]:
                            if nv > dp_next[w]:
                                dp_next[w] = nv
            # now ε-close dp_next itself
            for u in range(N):
                if dp_next[u] < 0:
                    continue
                val = dp_next[u]
                for w in closure[u]:
                    if val > dp_next[w]:
                        dp_next[w] = val

            dp = dp_next

        # 5) Answer is max over ε-closure(accept)
        ans = max(dp[u] for u in closure[accept])
        print(ans if ans >= 0 else -1)

if __name__ == "__main__":
    solve()
