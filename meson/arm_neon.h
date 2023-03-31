/* This file automatically "generated" by Meson. Please check when updating! */
#ifndef VPX_WIN_ARM_NEON_H_WORKAROUND
#define VPX_WIN_ARM_NEON_H_WORKAROUND
/* The Windows SDK has arm_neon.h, but unlike on other platforms it is
 * ARM32-only. ARM64 NEON support is provided by arm64_neon.h, a proper
 * superset of arm_neon.h. Work around this by providing a more local
 * arm_neon.h that simply #includes arm64_neon.h.
 */
#include <arm64_neon.h>
#endif /* VPX_WIN_ARM_NEON_H_WORKAROUND */
