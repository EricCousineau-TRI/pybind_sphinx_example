#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Yo
"""

def CalcPointsGeometricJacobianExpressedInWorld():
    """
    Given a set of points `Qi` with fixed position vectors `p_BQi` in a frame
    B, (that is, their time derivative `ᴮd/dt(p_BQi)` in frame B is zero),
    this method computes the geometric Jacobian `Jv_WQi` defined by:
    <pre>
      v_WQi(q, v) = Jv_WQi(q)⋅v
    </pre>
    where `p_WQi` is the position vector in the world frame for each point
    `Qi` in the input set, `v_WQi(q, v)` is the translational velocity of
    point `Qi` in the world frame W and q and v are the vectors of generalized
    position and velocity, respectively. Since the spatial velocity of each
    point `Qi` is linear in the generalized velocities, the geometric
    Jacobian `Jv_WQi` is a function of the generalized coordinates q only.

    @param[in] context
      The context containing the state of the model. It stores the
      generalized positions q.
    @param[in] frame_B
      The positions `p_BQi` of each point in the input set are measured and
      expressed in this frame B and are constant (fixed) in this frame.
    @param[in] p_BQi_set
      A matrix with the fixed position of a set of points `Qi` measured and
      expressed in `frame_B`.
      Each column of this matrix contains the position vector `p_BQi` for a
      point `Qi` measured and expressed in frame B. Therefore this input
      matrix lives in ℝ³ˣⁿᵖ with `np` the number of points in the set.
    @param[out] p_WQi_set
      The output positions of each point `Qi` now computed as measured and
      expressed in frame W. These positions are computed in the process of
      computing the geometric Jacobian `J_WQi` and therefore external storage
      must be provided.
      The output `p_WQi_set` **must** have the same size
      as the input set `p_BQi_set` or otherwise this method throws a
      std::runtime_error exception. That is `p_WQi_set` **must** be in
      `ℝ³ˣⁿᵖ`.
    @param[out] Jv_WQi
      The geometric Jacobian `Jv_WQi(q)`, function of the generalized
      positions q only. This Jacobian relates the translational velocity
      `v_WQi` of each point `Qi` in the input set by: <pre>
        `v_WQi(q, v) = Jv_WQi(q)⋅v`
      </pre>
      so that `v_WQi` is a column vector of size `3⋅np` concatenating the
      velocity of all points `Qi` in the same order they were given in the
      input set. Therefore `J_WQi` is a matrix of size `3⋅np x nv`, with `nv`
      the number of generalized velocities. On input, matrix `J_WQi` **must**
      have size `3⋅np x nv` or this method throws a std::runtime_error
      exception.

    @throws an exception if the output `p_WQi_set` is nullptr or does not have
    the same size as the input array `p_BQi_set`.
    @throws an exception if `Jv_WQi` is nullptr or if it does not have the
    appropriate size, see documentation for `Jv_WQi` for details.
    """
    pass


def SparseMatrixToRowColumnValueVectors():
    r"""
    the non-zero entries.
    For example, the matrix
    <!--
    mat = [1 0 2;
          [0 3 4]
    has row = [0 1 0 1]
        col = [0 1 2 2]
        val = [1 3 2 4]
    -->
    \f[
    mat = \begin{bmatrix} 1 & 0 & 2\\
                          0 & 3 & 4\end{bmatrix}
    \f]
    has
    \f[
    row = \begin{bmatrix} 0 & 1 & 0 & 1\end{bmatrix}\\
    col = \begin{bmatrix} 0 & 1 & 2 & 2\end{bmatrix}\\
    val = \begin{bmatrix} 1 & 3 & 2 & 4\end{bmatrix}
    \f]
    @param[in] matrix the input sparse matrix
    @param[out] row_indices a vector containing the row indices of the
    non-zero entries
    @param[out] col_indices a vector containing the column indices of the
    non-zero entries
    @param[out] val a vector containing the values of the non-zero entries.
    """
    pass