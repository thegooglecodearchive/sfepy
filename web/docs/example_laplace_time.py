from example_laplace import filename_mesh, options, materials, regions, \
     fields, ebcs, integrals, solvers, fe

options.update({
    'ts' : 'ts',
    'save_steps' : -1,
})

variables = {
    'u'   : ('unknown field', 'temperature', 0, 'previous'),
    'v'   : ('test field',    'temperature', 'u'),
}

equations = {
    'Laplace equation in time' :
    """dw_mass_scalar.i1.Omega( v, du/dt )
     + dw_laplace.i1.Omega( m.c, v, u ) = 0"""
}

solvers.update({
    'ts' : ('ts.simple',
            {'t0' : 0.0,
             't1' : 0.001,
             'dt' : None,
             'n_step' : 11
             }),
})

newton = solvers['newton']
newton[1].update({'problem' : 'linear'})

ls = solvers['ls']
ls[1].update({'presolve' : True})

print solvers
