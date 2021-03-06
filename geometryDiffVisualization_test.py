from geometryDiffVisualization import *

g1 = MuonGeometry("ideal_CHECK.xml")
g2 = MuonGeometry("antitwist_CHECK.xml")
draw_station(g1, g2, 1, "antitwist_station1.svg", length_factor=400., angle_factor=400.)
draw_station(g1, g2, 2, "antitwist_station2.svg", length_factor=400., angle_factor=400.)
draw_station(g1, g2, 3, "antitwist_station3.svg", length_factor=400., angle_factor=400.)
draw_station(g1, g2, 4, "antitwist_station4.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, -2, "antitwist_wheelm2.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, -1, "antitwist_wheelm1.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2,  0, "antitwist_wheelze.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, +1, "antitwist_wheelp1.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, +2, "antitwist_wheelp2.svg", length_factor=400., angle_factor=400.)

g1 = MuonGeometry("ideal_CHECK.xml")
g2 = MuonGeometry("antilocaly_CHECK.xml")
draw_station(g1, g2, 1, "antilocaly_station1.svg", length_factor=400., angle_factor=400.)
draw_station(g1, g2, 2, "antilocaly_station2.svg", length_factor=400., angle_factor=400.)
draw_station(g1, g2, 3, "antilocaly_station3.svg", length_factor=400., angle_factor=400.)
draw_station(g1, g2, 4, "antilocaly_station4.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, -2, "antilocaly_wheelm2.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, -1, "antilocaly_wheelm1.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2,  0, "antilocaly_wheelze.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, +1, "antilocaly_wheelp1.svg", length_factor=400., angle_factor=400.)
draw_wheel(g1, g2, +2, "antilocaly_wheelp2.svg", length_factor=400., angle_factor=400.)

g1 = MuonGeometry("/tmp/test_hardware.xml")
g2 = MuonGeometry("/tmp/test_trackbased.xml")
draw_station(g1, g2, 1, "/tmp/station1.svg", length_factor=200., angle_factor=200.)
draw_station(g1, g2, 2, "/tmp/station2.svg", length_factor=200., angle_factor=200.)
draw_station(g1, g2, 3, "/tmp/station3.svg", length_factor=200., angle_factor=200.)
draw_station(g1, g2, 4, "/tmp/station4.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, -2, "/tmp/wheelm2.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, -1, "/tmp/wheelm1.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2,  0, "/tmp/wheelze.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, +1, "/tmp/wheelp1.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, +2, "/tmp/wheelp2.svg", length_factor=200., angle_factor=200.)

g1 = MuonGeometry("/tmp/test_hardware.xml")
g2 = MuonGeometry("/tmp/test_hardware_plus_0_5_mrad_twist_otherdirection.xml")
draw_station(g1, g2, 1, "/tmp/station1.svg", length_factor=200., angle_factor=200.)
draw_station(g1, g2, 2, "/tmp/station2.svg", length_factor=200., angle_factor=200.)
draw_station(g1, g2, 3, "/tmp/station3.svg", length_factor=200., angle_factor=200.)
draw_station(g1, g2, 4, "/tmp/station4.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, -2, "/tmp/wheelm2.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, -1, "/tmp/wheelm1.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2,  0, "/tmp/wheelze.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, +1, "/tmp/wheelp1.svg", length_factor=200., angle_factor=200.)
draw_wheel(g1, g2, +2, "/tmp/wheelp2.svg", length_factor=200., angle_factor=200.)
