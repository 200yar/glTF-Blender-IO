"""
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Contributor(s): Julien Duroure.
 *
 * ***** END GPL LICENSE BLOCK *****
 * This development is done in strong collaboration with Airbus Defence & Space
 """

# Note that this class is not a glTF object
class PyAnimationBone():
    def __init__(self, animation):
        self.animation = animation

# Note that this class is not a glTF object
class PyAnimationNode():
    def __init__(self, animation):
        self.animation = animation

# Note that this class is not a glTF object
class PyAnimationData():
    def __init__(self, node, gltf):
        self.node = node
        self.gltf = gltf
        self.anims = {}
        self.node_anim = PyAnimationNode(self)
        self.bone_anim = PyAnimationBone(self)
