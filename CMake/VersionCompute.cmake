# Load version number components.
include (${CMAKE_SOURCE_DIR}/Versions.cmake)

# Compute the full version string.
set (WSJTX_VERSION_PATCH ${WSJTX_VERSION_SUB})
if (WSJTX_VERSION_32A)
    set (WSJTX_VERSION_PATCH ${WSJTX_VERSION_PATCH}-32A)
    set (BUILD_TYPE_REVISION ${BUILD_TYPE_REVISION}-32A)
endif (WSJTX_VERSION_32A)

if (WSJTX_RC AND NOT WSJTX_VERSION_IS_RELEASE)
    set (WSJTX_VERSION_PATCH ${WSJTX_VERSION_PATCH}-rc${WSJTX_RC})
    set (BUILD_TYPE_REVISION ${BUILD_TYPE_REVISION}-rc${WSJTX_RC})
endif (WSJTX_RC AND NOT WSJTX_VERSION_IS_RELEASE)

set (wsjtx_VERSION ${WSJTX_VERSION_MAJOR}.${WSJTX_VERSION_MINOR}.${WSJTX_VERSION_PATCH})
