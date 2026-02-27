from equations.lattice_eqs import (
    f_constant,
    unit_cell_volume_sq,
    metric_tensor,
    reciprocal_metric_tensor,
)

from equations.plane_eqs import (
    planes_identification,
    plane_vector_magnitude,
    two_shortest_planes,
    plane_angles,
)

equation_map = {
    "f_constant": f_constant,
    "unit_cell_volume_sq": unit_cell_volume_sq,
    "metric_tensor": metric_tensor,
    "reciprocal_metric_tensor": reciprocal_metric_tensor,
    "planes_identification": planes_identification,
    "plane_vector_magnitude": plane_vector_magnitude,
    "two_shortest_planes": two_shortest_planes,
    "plane_angles": plane_angles,
}