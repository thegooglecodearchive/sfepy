filename_mesh = 'simple.mesh'

options = {
    'nls' : 'newton',
    'ls' : 'ls',
}

materials = {
    'm' : ('here', 'Omega', {'c' : 1.0}),
}

regions = {
    'Omega' : ('all', {}),
    'Gamma_Left' : ('nodes in (x < 0.00001)', {}),
    'Gamma_Right' : ('nodes in (x > 0.099999)', {}),
}

fields = {
    'temperature' : ((1,1), 'real', 'Omega', {'Omega' : '3_4_P1'}),
}

variables = {
    'u'   : ('unknown field', 'temperature', 0),
    'v'   : ('test field',    'temperature', 'u'),
}

ebcs = {
    'u1' : ('Gamma_Left', {'u.0' : 2.0}),
    'u2' : ('Gamma_Right', {'u.0' : -2.0}),
}

integrals = {
    'i1' : ('v', 'gauss_o1_d3'),
}

equations = {
    'Laplace equation' : 'dw_laplace.i1.Omega( m.c, v, u ) = 0'
}

solvers = {
    'ls' : ('ls.scipy_direct', {}),
    'newton' : ('nls.newton',
                {'i_max'      : 1,
                 'eps_a'      : 1e-10,
                 }),
}

fe = {
    'chunk_size' : 100000
}
