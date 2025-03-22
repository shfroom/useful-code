import SwiftUI
import SceneKit

struct CustomSceneView: NSViewRepresentable {
    @Environment(\.colorScheme) var colorScheme
    var sceneName: String // Parameter to hold the scene file name
    
    func makeNSView(context: Context) -> SCNView {
        let scnView = SCNView()
        if let scene = SCNScene(named: sceneName) { // Use the sceneName parameter
            scnView.scene = scene
        } else {
            print("Error: \(sceneName) file not found")
        }
        scnView.allowsCameraControl = true
        scnView.autoenablesDefaultLighting = true
        scnView.backgroundColor = NSColor.clear
        return scnView
    }
    
    func updateNSView(_ nsView: SCNView, context: Context) {
        // Update the view during state changes, if necessary
    }
}
￼

CustomSceneView(sceneName: sceneNames[objectNum])
                    .frame(height: 400)
                    .id(objectNum)