import sympy

def apply_ics(sol, ics, x, known_params):
	"""
	Apply the initial conditions (ics), given as a dictionary on
	the form ics = {y(0): y0, y(x).diff(x).subs(x, 0): yp0, ...},
	to the solution of the ODE with independent variable x.
	The undetermined integration constants C1, C2, ... are extracted
	from the free symbols of the ODE solution, excluding symbols in
	the known_params list.
	"""

	free_params = sol.free_symbols - set(known_params)
	eqs = [(sol.lhs.diff(x, n) - sol.rhs.diff(x, n)).subs(x, 0).subs(ics) for n in range(len(ics))]
	sol_params = sympy.solve(eqs, free_params)

	return sol.subs(sol_params)

sympy.init_printing()
## initialize the print environment
t, omega0, gamma = sympy.symbols("t, omega_0, gamma", positive=True)
## symbolize the parameters and they can only be positive
x = sympy.Function('x')
## set x to be the differential function, not the variable
ode = x(t).diff(t, 2) + 2 * gamma * omega0 * x(t).diff(t) + omega0**2*x(t)
ode_sol = sympy.dsolve(ode)
## use diff() and dsolve to get the general solution
ics = {x(0): 1, x(t).diff(t).subs(t, 0): 0}
## apply dict to the initial conditions
x_t_sol = apply_ics(ode_sol, ics, t, [omega0, gamma])
## get the solution with ics by calling function apply_ics.
sympy.pprint(x_t_sol)

