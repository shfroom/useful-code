//
//  ContentView.swift
//  Hello World
//
//  Created by Shaunak Ghosh on 25/02/2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            Sidebar()
            MainContentView()
        }
        .frame(minWidth: 800, minHeight: 600)
    }
}

struct Sidebar: View {
    var body: some View {
        List {
            NavigationLink(destination: EarthView()) {
                Label("Planet Earth", systemImage: "globe")
            }
            NavigationLink(destination: OrbitView()) {
                Label("Objects in Orbit", systemImage: "circle")
            }
            NavigationLink(destination: SolarSystemView()) {
                Label("The Solar System", systemImage: "sun.max")
            }
        }
        .listStyle(SidebarListStyle())
        .frame(minWidth: 200, idealWidth: 250, maxWidth: 300)
        .toolbar {
            ToolbarItem(placement: .automatic) {
                Button(action: toggleSidebar) {
                    Label("Toggle Sidebar", systemImage: "sidebar.left")
                }
            }
        }
    }
    
    private func toggleSidebar() {
        NSApp.keyWindow?.firstResponder?.tryToPerform(#selector(NSSplitViewController.toggleSidebar(_:)), with: nil)
    }
}

struct MainContentView: View {
    var body: some View {
        Text("Select an item from the sidebar")
            .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}
