# Copyright (c) 2021 NVIDIA CORPORATION.  All rights reserved.
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

no_grad = False         # disable adjoint tracking
check_grad = False      # will perform numeric gradient checking after each launch
verify_fp = False       # verify inputs and outputs are finite after each launch
