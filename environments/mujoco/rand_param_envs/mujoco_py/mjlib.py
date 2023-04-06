import os
import sys

from environments.mujoco.rand_param_envs.mujoco_py import config

from .mjtypes import *
from .util import *

path_prefix = config.mjpro_path
if sys.platform.startswith("darwin"):
    libfile = os.path.join(path_prefix, "bin/libmujoco131.dylib")
elif sys.platform.startswith("linux"):
    libfile = os.path.join(path_prefix, "bin/libmujoco131.so")
elif sys.platform.startswith("win"):
    libfile = os.path.join(path_prefix, "bin/mujoco131.lib")
else:
    raise RuntimeError("Unrecognized platform %s" % sys.platform)

if not os.path.exists(libfile):
    raise RuntimeError(
        "Missing path: %s. (HINT: you should have unzipped the mjpro131.zip bundle without modification.)"
        % libfile
    )

mjlib = cdll.LoadLibrary(os.path.abspath(libfile))

mjlib.mj_loadXML.argtypes = [String, String, c_char_p, c_int]
mjlib.mj_loadXML.restype = POINTER(MJMODEL)
mjlib.mj_saveXML.argtypes = [String, POINTER(MJMODEL), String]
mjlib.mj_saveXML.restype = c_int
# mjlib.mj_printSchema.argtypes = [String, String, c_int, c_int, c_int]
# mjlib.mj_printSchema.restype = c_int
mjlib.mj_activate.argtypes = [String]
mjlib.mj_activate.restype = c_int
mjlib.mj_step.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
mjlib.mj_step.restype = None
mjlib.mj_step1.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
mjlib.mj_step1.restype = None
mjlib.mj_step2.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
mjlib.mj_step2.restype = None
mjlib.mj_forward.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
mjlib.mj_forward.restype = None
# mjlib.mj_inverse.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_inverse.restype = None
# mjlib.mj_forwardSkip.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int]
# mjlib.mj_forwardSkip.restype = None
# mjlib.mj_inverseSkip.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int]
# mjlib.mj_inverseSkip.restype = None
# mjlib.mj_sensor.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_sensor.restype = None
# mjlib.mj_energy.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_energy.restype = None
# mjlib.mj_defaultSolRefImp.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mj_defaultSolRefImp.restype = None
# mjlib.mj_defaultOption.argtypes = [POINTER(mjOption)]
# mjlib.mj_defaultOption.restype = None
# mjlib.mj_defaultVisual.argtypes = [POINTER(mjVisual)]
# mjlib.mj_defaultVisual.restype = None
# mjlib.mj_copyModel.argtypes = [POINTER(MJMODEL), POINTER(MJMODEL)]
# mjlib.mj_copyModel.restype = POINTER(MJMODEL)
# mjlib.mj_saveModel.argtypes = [POINTER(MJMODEL), String, c_int, POINTER(None)]
# mjlib.mj_saveModel.restype = None
# mjlib.mj_loadModel.argtypes = [String, c_int, POINTER(None)]
# mjlib.mj_loadModel.restype = POINTER(MJMODEL)
mjlib.mj_deleteModel.argtypes = [POINTER(MJMODEL)]
mjlib.mj_deleteModel.restype = None
# mjlib.mj_sizeModel.argtypes = [POINTER(MJMODEL)]
# mjlib.mj_sizeModel.restype = c_int
mjlib.mj_makeData.argtypes = [POINTER(MJMODEL)]
mjlib.mj_makeData.restype = POINTER(MJDATA)
# mjlib.mj_copyData.argtypes = [POINTER(MJDATA), POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_copyData.restype = POINTER(MJDATA)
mjlib.mj_resetData.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
mjlib.mj_resetData.restype = None
# mjlib.mj_stackAlloc.argtypes = [POINTER(MJDATA), c_int]
# mjlib.mj_stackAlloc.restype = POINTER(c_double)
mjlib.mj_deleteData.argtypes = [POINTER(MJDATA)]
mjlib.mj_deleteData.restype = None
# mjlib.mj_resetCallbacks.argtypes = []
# mjlib.mj_resetCallbacks.restype = None
# mjlib.mj_setConst.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int]
# mjlib.mj_setConst.restype = None
# mjlib.mj_printModel.argtypes = [POINTER(MJMODEL), String]
# mjlib.mj_printModel.restype = None
# mjlib.mj_printData.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), String]
# mjlib.mj_printData.restype = None
# mjlib.mju_printMat.argtypes = [POINTER(c_double), c_int, c_int]
# mjlib.mju_printMat.restype = None
# mjlib.mj_fwdPosition.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_fwdPosition.restype = None
# mjlib.mj_fwdVelocity.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_fwdVelocity.restype = None
# mjlib.mj_fwdActuation.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_fwdActuation.restype = None
# mjlib.mj_fwdAcceleration.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_fwdAcceleration.restype = None
# mjlib.mj_fwdConstraint.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_fwdConstraint.restype = None
# mjlib.mj_Euler.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_Euler.restype = None
# mjlib.mj_RungeKutta.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int]
# mjlib.mj_RungeKutta.restype = None
# mjlib.mj_invPosition.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_invPosition.restype = None
# mjlib.mj_invVelocity.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_invVelocity.restype = None
# mjlib.mj_invConstraint.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_invConstraint.restype = None
# mjlib.mj_compareFwdInv.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_compareFwdInv.restype = None
# mjlib.mj_checkPos.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_checkPos.restype = None
# mjlib.mj_checkVel.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_checkVel.restype = None
# mjlib.mj_checkAcc.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_checkAcc.restype = None
# mjlib.mj_kinematics.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_kinematics.restype = None
# mjlib.mj_comPos.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_comPos.restype = None
# mjlib.mj_tendon.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_tendon.restype = None
# mjlib.mj_transmission.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_transmission.restype = None
# mjlib.mj_crb.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_crb.restype = None
# mjlib.mj_factorM.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_factorM.restype = None
# mjlib.mj_backsubM.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_backsubM.restype = None
# mjlib.mj_backsubM2.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_backsubM2.restype = None
# mjlib.mj_comVel.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_comVel.restype = None
# mjlib.mj_passive.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_passive.restype = None
# mjlib.mj_rne.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int, POINTER(c_double)]
# mjlib.mj_rne.restype = None
# mjlib.mj_rnePostConstraint.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_rnePostConstraint.restype = None
# mjlib.mj_collision.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_collision.restype = None
# mjlib.mj_makeConstraint.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_makeConstraint.restype = None
# mjlib.mj_projectConstraint.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_projectConstraint.restype = None
# mjlib.mj_referenceConstraint.argtypes = [POINTER(MJMODEL), POINTER(MJDATA)]
# mjlib.mj_referenceConstraint.restype = None
# mjlib.mj_isPyramid.argtypes = [POINTER(MJMODEL)]
# mjlib.mj_isPyramid.restype = c_int
# mjlib.mj_isSparse.argtypes = [POINTER(MJMODEL)]
# mjlib.mj_isSparse.restype = c_int
# mjlib.mj_mulJacVec.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double)]
# mjlib.mj_mulJacVec.restype = None
# mjlib.mj_mulJacTVec.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double)]
# mjlib.mj_mulJacTVec.restype = None
# mjlib.mj_jac.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_jac.restype = None
# mjlib.mj_jacBody.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_jacBody.restype = None
# mjlib.mj_jacBodyCom.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_jacBodyCom.restype = None
# mjlib.mj_jacGeom.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_jacGeom.restype = None
# mjlib.mj_jacSite.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_jacSite.restype = None
# mjlib.mj_jacPointAxis.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_jacPointAxis.restype = None
mjlib.mj_name2id.argtypes = [
    POINTER(MJMODEL),
    c_int,
    String,
]  # The middle term is a mjtObj (an enum) in C.
mjlib.mj_name2id.restype = c_int
# mjlib.mj_id2name.argtypes = [POINTER(MJMODEL), mjtObj, c_int]
# mjlib.    mj_id2name.restype = ReturnString
# mjlib.else:
# mjlib.    mj_id2name.restype = String
# mjlib.    mj_id2name.errcheck = ReturnString
# mjlib.mj_fullM.argtypes = [POINTER(MJMODEL), POINTER(c_double), POINTER(c_double)]
# mjlib.mj_fullM.restype = None
# mjlib.mj_mulM.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double)]
# mjlib.mj_mulM.restype = None
# mjlib.mj_applyFT.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, POINTER(c_double)]
# mjlib.mj_applyFT.restype = None
# mjlib.mj_objectVelocity.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int, c_int, POINTER(c_double), mjtByte]
# mjlib.mj_objectVelocity.restype = None
# mjlib.mj_objectAcceleration.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int, c_int, POINTER(c_double), mjtByte]
# mjlib.mj_objectAcceleration.restype = None
# mjlib.mj_contactForce.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int, POINTER(c_double)]
# mjlib.mj_contactForce.restype = None
# mjlib.mj_integratePos.argtypes = [POINTER(MJMODEL), POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mj_integratePos.restype = None
# mjlib.mj_normalizeQuat.argtypes = [POINTER(MJMODEL), POINTER(c_double)]
# mjlib.mj_normalizeQuat.restype = None
# mjlib.mj_local2Global.argtypes = [POINTER(MJDATA), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mj_local2Global.restype = None
# mjlib.mj_getTotalmass.argtypes = [POINTER(MJMODEL)]
# mjlib.mj_getTotalmass.restype = c_double
# mjlib.mj_setTotalmass.argtypes = [POINTER(MJMODEL), c_double]
# mjlib.mj_setTotalmass.restype = None
# mjlib.mj_version.argtypes = []
# mjlib.mj_version.restype = c_double
mjlib.mjv_makeObjects.argtypes = [POINTER(MJVOBJECTS), c_int]
mjlib.mjv_makeObjects.restype = None
mjlib.mjv_freeObjects.argtypes = [POINTER(MJVOBJECTS)]
mjlib.mjv_freeObjects.restype = None
mjlib.mjv_defaultOption.argtypes = [POINTER(MJVOPTION)]
mjlib.mjv_defaultOption.restype = None
# mjlib.mjv_defaultCameraPose.argtypes = [POINTER(MJVCAMERAPOSE)]
# mjlib.mjv_defaultCameraPose.restype = None
mjlib.mjv_defaultCamera.argtypes = [POINTER(MJVCAMERA)]
mjlib.mjv_defaultCamera.restype = None
mjlib.mjv_setCamera.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(MJVCAMERA)]
mjlib.mjv_setCamera.restype = None
mjlib.mjv_updateCameraPose.argtypes = [POINTER(MJVCAMERA), c_double]
mjlib.mjv_updateCameraPose.restype = None
# mjlib.mjv_convert3D.argtypes = [POINTER(c_double), POINTER(c_double), c_double, POINTER(MJVCAMERAPOSE)]
# mjlib.mjv_convert3D.restype = None
# mjlib.mjv_convert2D.argtypes = [POINTER(c_double), mjtMouse, c_double, c_double, c_double, POINTER(MJVCAMERAPOSE)]
# mjlib.mjv_convert2D.restype = None
mjlib.mjv_moveCamera.argtypes = [
    c_int,
    c_float,
    c_float,
    POINTER(MJVCAMERA),
    c_float,
    c_float,
]
mjlib.mjv_moveCamera.restype = None
# mjlib.mjv_moveObject.argtypes = [mjtMouse, c_float, c_float, POINTER(MJVCAMERAPOSE), c_float, c_float, POINTER(c_double), POINTER(c_double)]
# mjlib.mjv_moveObject.restype = None
mjlib.mjv_mousePerturb.argtypes = [
    POINTER(MJMODEL),
    POINTER(MJDATA),
    c_int,
    c_int,
    POINTER(c_double),
    POINTER(c_double),
    POINTER(c_double),
]
mjlib.mjv_mousePerturb.restype = None
# mjlib.mjv_mouseEdit.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), c_int, c_int, POINTER(c_double), POINTER(c_double)]
# mjlib.mjv_mouseEdit.restype = None
mjlib.mjv_makeGeoms.argtypes = [
    POINTER(MJMODEL),
    POINTER(MJDATA),
    POINTER(MJVOBJECTS),
    POINTER(MJVOPTION),
    c_int,
    c_int,
    POINTER(c_double),
    POINTER(c_double),
    POINTER(c_double),
]
mjlib.mjv_makeGeoms.restype = None
mjlib.mjv_makeLights.argtypes = [POINTER(MJMODEL), POINTER(MJDATA), POINTER(MJVOBJECTS)]
mjlib.mjv_makeLights.restype = None
mjlib.mjr_overlay.argtypes = [
    MJRRECT,
    c_int,
    c_int,
    String,
    String,
    POINTER(MJRCONTEXT),
]
mjlib.mjr_overlay.restype = None
# mjlib.mjr_rectangle.argtypes = [c_int, MJRRECT, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
# mjlib.mjr_rectangle.restype = None
# mjlib.mjr_finish.argtypes = []
# mjlib.mjr_finish.restype = None
# mjlib.mjr_text.argtypes = [String, POINTER(MJRCONTEXT), c_int, c_float, c_float, c_float, c_float, c_float, c_float]
# mjlib.mjr_text.restype = None
# mjlib.mjr_textback.argtypes = [String, POINTER(MJRCONTEXT), c_float, c_float, c_float, c_float, c_float, c_float]
# mjlib.mjr_textback.restype = None
# mjlib.mjr_textWidth.argtypes = [String, POINTER(MJRCONTEXT), c_int]
# mjlib.mjr_textWidth.restype = c_int
mjlib.mjr_defaultOption.argtypes = [POINTER(MJROPTION)]
mjlib.mjr_defaultOption.restype = None
mjlib.mjr_defaultContext.argtypes = [POINTER(MJRCONTEXT)]
mjlib.mjr_defaultContext.restype = None
# mjlib.mjr_uploadTexture.argtypes = [POINTER(MJMODEL), POINTER(MJRCONTEXT), c_int]
# mjlib.mjr_uploadTexture.restype = None
mjlib.mjr_makeContext.argtypes = [POINTER(MJMODEL), POINTER(MJRCONTEXT), c_int]
mjlib.mjr_makeContext.restype = None
mjlib.mjr_freeContext.argtypes = [POINTER(MJRCONTEXT)]
mjlib.mjr_freeContext.restype = None
mjlib.mjr_render.argtypes = [
    c_int,
    MJRRECT,
    POINTER(MJVOBJECTS),
    POINTER(MJROPTION),
    POINTER(MJVCAMERAPOSE),
    POINTER(MJRCONTEXT),
]
mjlib.mjr_render.restype = None
# mjlib.mjr_select.argtypes = [MJRRECT, POINTER(MJVOBJECTS), c_int, c_int, POINTER(c_double), POINTER(c_double), POINTER(MJROPTION), POINTER(MJVCAMERAPOSE), POINTER(MJRCONTEXT)]
# mjlib.mjr_select.restype = c_int
# mjlib.mjr_showOffscreen.argtypes = [c_int, c_int, POINTER(MJRCONTEXT)]
# mjlib.mjr_showOffscreen.restype = None
# mjlib.mjr_showBuffer.argtypes = [POINTER(c_ubyte), c_int, c_int, c_int, c_int, POINTER(MJRCONTEXT)]
# mjlib.mjr_showBuffer.restype = None
# mjlib.mjr_getOffscreen.argtypes = [POINTER(c_ubyte), POINTER(c_float), MJRRECT, POINTER(MJRCONTEXT)]
# mjlib.mjr_getOffscreen.restype = None
# mjlib.mjr_getBackbuffer.argtypes = [POINTER(c_ubyte), POINTER(c_float), MJRRECT, POINTER(MJRCONTEXT)]
# mjlib.mjr_getBackbuffer.restype = None
# mjlib.
# mjlib.
# mjlib.mju_error.argtypes = [String]
# mjlib.mju_error.restype = None
# mjlib.mju_error_i.argtypes = [String, c_int]
# mjlib.mju_error_i.restype = None
# mjlib.mju_error_s.argtypes = [String, String]
# mjlib.mju_error_s.restype = None
# mjlib.mju_warning.argtypes = [String]
# mjlib.mju_warning.restype = None
# mjlib.mju_warning_i.argtypes = [String, c_int]
# mjlib.mju_warning_i.restype = None
# mjlib.mju_warning_s.argtypes = [String, String]
# mjlib.mju_warning_s.restype = None
# mjlib.mju_clearHandlers.argtypes = []
# mjlib.mju_clearHandlers.restype = None
# mjlib.mju_malloc.argtypes = [c_size_t]
# mjlib.mju_malloc.restype = POINTER(None)
# mjlib.mju_free.argtypes = [POINTER(None)]
# mjlib.mju_free.restype = None
# mjlib.mj_warning.argtypes = [POINTER(MJDATA), c_int]
# mjlib.mj_warning.restype = None
# mjlib.mju_zero3.argtypes = [POINTER(c_double)]
# mjlib.mju_zero3.restype = None
# mjlib.mju_copy3.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_copy3.restype = None
# mjlib.mju_scl3.argtypes = [POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mju_scl3.restype = None
# mjlib.mju_add3.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_add3.restype = None
# mjlib.mju_sub3.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_sub3.restype = None
# mjlib.mju_addTo3.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_addTo3.restype = None
# mjlib.mju_addToScl3.argtypes = [POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mju_addToScl3.restype = None
# mjlib.mju_addScl3.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mju_addScl3.restype = None
# mjlib.mju_normalize3.argtypes = [POINTER(c_double)]
# mjlib.mju_normalize3.restype = c_double
# mjlib.mju_norm3.argtypes = [POINTER(c_double)]
# mjlib.mju_norm3.restype = c_double
# mjlib.mju_dot3.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_dot3.restype = c_double
# mjlib.mju_dist3.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_dist3.restype = c_double
# mjlib.mju_rotVecMat.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_rotVecMat.restype = None
# mjlib.mju_rotVecMatT.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_rotVecMatT.restype = None
# mjlib.mju_cross.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_cross.restype = None
# mjlib.mju_zero.argtypes = [POINTER(c_double), c_int]
# mjlib.mju_zero.restype = None
# mjlib.mju_copy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_copy.restype = None
# mjlib.mju_scl.argtypes = [POINTER(c_double), POINTER(c_double), c_double, c_int]
# mjlib.mju_scl.restype = None
# mjlib.mju_add.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_add.restype = None
# mjlib.mju_sub.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_sub.restype = None
# mjlib.mju_addTo.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_addTo.restype = None
# mjlib.mju_addToScl.argtypes = [POINTER(c_double), POINTER(c_double), c_double, c_int]
# mjlib.mju_addToScl.restype = None
# mjlib.mju_addScl.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_int]
# mjlib.mju_addScl.restype = None
# mjlib.mju_normalize.argtypes = [POINTER(c_double), c_int]
# mjlib.mju_normalize.restype = c_double
# mjlib.mju_norm.argtypes = [POINTER(c_double), c_int]
# mjlib.mju_norm.restype = c_double
# mjlib.mju_dot.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_dot.restype = c_double
# mjlib.mju_mulMatVec.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_int]
# mjlib.mju_mulMatVec.restype = None
# mjlib.mju_mulMatTVec.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_int]
# mjlib.mju_mulMatTVec.restype = None
# mjlib.mju_transpose.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_int]
# mjlib.mju_transpose.restype = None
# mjlib.mju_mulMatMat.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int]
# mjlib.mju_mulMatMat.restype = None
# mjlib.mju_mulMatMatT.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int]
# mjlib.mju_mulMatMatT.restype = None
# mjlib.mju_sqrMat.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_int, POINTER(c_double), c_int]
# mjlib.mju_sqrMat.restype = None
# mjlib.mju_mulMatTMat.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int]
# mjlib.mju_mulMatTMat.restype = None
# mjlib.mju_transformSpatial.argtypes = [POINTER(c_double), POINTER(c_double), mjtByte, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_transformSpatial.restype = None
# mjlib.mju_rotVecQuat.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_rotVecQuat.restype = None
# mjlib.mju_negQuat.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_negQuat.restype = None
# mjlib.mju_mulQuat.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_mulQuat.restype = None
# mjlib.mju_mulQuatAxis.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_mulQuatAxis.restype = None
# mjlib.mju_axisAngle2Quat.argtypes = [POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mju_axisAngle2Quat.restype = None
# mjlib.mju_quat2Vel.argtypes = [POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mju_quat2Vel.restype = None
# mjlib.mju_quat2Mat.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_quat2Mat.restype = None
# mjlib.mju_mat2Quat.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_mat2Quat.restype = None
# mjlib.mju_derivQuat.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_derivQuat.restype = None
# mjlib.mju_quatIntegrate.argtypes = [POINTER(c_double), POINTER(c_double), c_double]
# mjlib.mju_quatIntegrate.restype = None
# mjlib.mju_quatZ2Vec.argtypes = [POINTER(c_double), POINTER(c_double)]
# mjlib.mju_quatZ2Vec.restype = None
# mjlib.mju_cholFactor.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_double, c_double, POINTER(c_double)]
# mjlib.mju_cholFactor.restype = c_int
# mjlib.mju_cholBacksub.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int]
# mjlib.mju_cholBacksub.restype = None
# mjlib.mju_eig3.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
# mjlib.mju_eig3.restype = c_int
# mjlib.mju_muscleFVL.argtypes = [c_double, c_double, c_double, c_double, POINTER(c_double)]
# mjlib.mju_muscleFVL.restype = c_double
# mjlib.mju_musclePassive.argtypes = [c_double, c_double, c_double, POINTER(c_double)]
# mjlib.mju_musclePassive.restype = c_double
# mjlib.mju_pneumatic.argtypes = [c_double, c_double, c_double, POINTER(c_double), c_double, c_double, c_double, POINTER(c_double)]
# mjlib.mju_pneumatic.restype = c_double
# mjlib.mju_encodePyramid.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_encodePyramid.restype = None
# mjlib.mju_decodePyramid.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
# mjlib.mju_decodePyramid.restype = None
# mjlib.mju_springDamper.argtypes = [c_double, c_double, c_double, c_double, c_double]
# mjlib.mju_springDamper.restype = c_double
# mjlib.mju_min.argtypes = [c_double, c_double]
# mjlib.mju_min.restype = c_double
# mjlib.mju_max.argtypes = [c_double, c_double]
# mjlib.mju_max.restype = c_double
# mjlib.mju_sign.argtypes = [c_double]
# mjlib.mju_sign.restype = c_double
# mjlib.mju_round.argtypes = [c_double]
# mjlib.mju_round.restype = c_int
# mjlib.mju_type2Str.argtypes = [c_int]
# mjlib.    mju_type2Str.restype = ReturnString
# mjlib.else:
# mjlib.    mju_type2Str.restype = String
# mjlib.    mju_type2Str.errcheck = ReturnString
# mjlib.mju_str2Type.argtypes = [String]
# mjlib.mju_str2Type.restype = mjtObj
# mjlib.mju_warningText.argtypes = [c_int]
# mjlib.    mju_warningText.restype = ReturnString
# mjlib.else:
# mjlib.    mju_warningText.restype = String
# mjlib.    mju_warningText.errcheck = ReturnString
# mjlib.mju_isBad.argtypes = [c_double]
# mjlib.mju_isBad.restype = c_int
# mjlib.mju_isZero.argtypes = [POINTER(c_double), c_int]
# mjlib.mju_isZero.restype = c_int
