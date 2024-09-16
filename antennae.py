from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

colors = {0 : 'f1', 1 : 'f2', 2 : 'f3'}

# add nodes
Antenna1 = model.NewIntVar(0,2, "A1")
Antenna2 = model.NewIntVar(0,2, "A2")
Antenna3 = model.NewIntVar(0,2, "A3")
Antenna4 = model.NewIntVar(0,2, "A4")
Antenna5 = model.NewIntVar(0,2, "A5")
Antenna6 = model.NewIntVar(0,2, "A6")
Antenna7 = model.NewIntVar(0,2, "A7")
Antenna8 = model.NewIntVar(0,2, "A8")
Antenna9 = model.NewIntVar(0,2, "A9")

# add edges
model.Add(Antenna1 != Antenna2)
model.Add(Antenna1 != Antenna3)
model.Add(Antenna1 != Antenna4)

model.Add(Antenna2 != Antenna3)
model.Add(Antenna2 != Antenna5)
model.Add(Antenna2 != Antenna6)

model.Add(Antenna3 != Antenna6)
model.Add(Antenna3 != Antenna9)

model.Add(Antenna4 != Antenna5)

model.Add(Antenna6 != Antenna7)
model.Add(Antenna6 != Antenna8)

model.Add(Antenna7 != Antenna8)

model.Add(Antenna8 != Antenna9)

status = solver.Solve(model)

def antennae_submission():
  print("* antennae_submission *\n")
  if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
      print("Antenna 1: %s" % colors[solver.Value(Antenna1)])
      print("Antenna 2: %s" % colors[solver.Value(Antenna2)])
      print("Antenna 3: %s" % colors[solver.Value(Antenna3)])
      print("Antenna 4: %s" % colors[solver.Value(Antenna4)])
      print("Antenna 5: %s" % colors[solver.Value(Antenna5)])
      print("Antenna 6: %s" % colors[solver.Value(Antenna6)])
      print("Antenna 7: %s" % colors[solver.Value(Antenna7)])
      print("Antenna 8: %s" % colors[solver.Value(Antenna8)])
      print("Antenna 9: %s" % colors[solver.Value(Antenna9)])