# NOTE: this example needs RViz to be installed
# usage: start ROS master (roscore) and then run this test

import pinocchio as pin
from os.path import dirname, join, abspath

from pinocchio.visualize import RVizVisualizer

# Load the URDF model.
# Conversion with str seems to be necessary when executing this file with ipython
pinocchio_model_dir = join(dirname(dirname(str(abspath(__file__)))), "models")

mesh_dir = "robot_description"
urdf_model_path = "robot_description/inspirehand_R/urdf/R_inspire.urdf"

model, collision_model, visual_model = pin.buildModelsFromUrdf(
    urdf_model_path
)
viz = RVizVisualizer(model, collision_model, visual_model)

# Initialize the viewer.
viz.initViewer()
viz.loadViewerModel("pinocchio")

# Display a robot configuration.
q0 = pin.neutral(model)
viz.display(q0)

# Display another robot.
viz2 = RVizVisualizer(model, collision_model, visual_model)
viz2.initViewer(viz.viewer)
viz2.loadViewerModel(rootNodeName="pinocchio2")
q = q0.copy()
q[1] = 1.0
viz2.display(q)

input("Press enter to exit...")

viz.clean()