import argparse
import json
from FJE.JSONTreeBuilder import JSONTreeBuilder
from FJE.JSONVisualizer import JSONVisualizer
from FJE.Renderer.RendererAbstractFactory import RendererAbstractFactory
from FJE.Icon.IconFamily import IconFamily

def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer (FJE)')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
    parser.add_argument('-c', '--config', type=str, required=True, help='Path to configuration file')

    args = parser.parse_args()

    with open(args.file, 'r') as file:
        json_obj = json.load(file)

    with open(args.config, 'r', encoding='utf-8') as file:
        config = json.load(file)
    
    builder = JSONTreeBuilder()
    root = builder.build_tree(json_obj)

    style = config['style']
    node_icon = config['icon']['node']
    leaf_icon = config['icon']['leaf']
    icons = IconFamily(node_icon=node_icon, leaf_icon=leaf_icon)

    rendererFactory = RendererAbstractFactory.create_RendererFactory(style, icons)
    renderer = rendererFactory.createRenderer()
    visualizer = JSONVisualizer(renderer)
    visualizer.visualize(root)

if __name__ == "__main__":
    main()
