# Optimal Power Flow for Three-Bus System

This project uses Pyomo to solve an Optimal Power Flow (OPF) problem for a three-bus power system. The model minimizes generation costs while adhering to system constraints such as power flow limits, generator capacities, and load demands.

## Features
- Abstract model using Pyomo.
- Cost function and constraint-based optimization.
- Supports nonlinear solvers like IPOPT.
- Reads system data from an Excel file (`opfthreebus.xlsx`).

## Requirements
- Python 3.x
- Libraries: `pyomo`, `pandas`, `openpyxl`
- Solver: IPOPT

## Input File
`opfthreebus.xlsx`:
- `bus_num`: Bus numbers.
- `a`: Cost coefficients.
- `Pmax`: Maximum generation.
- `Pmin`: Minimum generation.
- `Pd`: Load demand.
- `imp`: Impedance matrix.


## Outputs
- Optimal power generation for each bus.
- Voltage angles (theta) for each bus.
- Results written to the console and formatted output via Pyomo.

## License
Open source, MIT License.
