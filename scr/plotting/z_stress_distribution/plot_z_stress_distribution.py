# imports
import os

import glob
import pandas as pd
import matplotlib.pyplot as plt

Params = {'backend': 'ps',
          'text.usetex': False}
plt.rcParams.update(Params)

FigParams = {'figure.figsize': [11, 6],
             'figure.autolayout': True,
             'figure.dpi': 300,
             'figure.frameon': True,
             'figure.facecolor': 'white',
             'figure.edgecolor': 'white'}
plt.rcParams.update(FigParams)

LegendParams = {'legend.loc': 'upper left',
                'legend.frameon': True,
                'legend.framealpha': 1,
                'legend.facecolor': 'inherit',
                'legend.edgecolor': 'black',
                'legend.fancybox': False,
                'legend.shadow': False,
                'legend.markerscale': 1,
                'legend.fontsize': 24,
                'legend.title_fontsize': 24,
                'legend.labelspacing': 0.5,
                'legend.columnspacing': 2.0}
plt.rcParams.update(LegendParams)

AxesParams = {'axes.facecolor': 'white',
              'axes.edgecolor': 'black',
              'axes.linewidth': 1.5,
              'axes.grid': True,
              'axes.grid.axis': 'both',
              'axes.labelsize': 24,
              'axes.labelpad': 4.0,
              'axes.formatter.limits': [-2, 3],
              'axes.formatter.use_locale': False,
              'axes.formatter.use_mathtext': False,
              'axes.formatter.useoffset': True,
              'axes.formatter.offset_threshold': 4,
              'axes.spines.left': True,
              'axes.spines.bottom': True,
              'axes.spines.right': True,
              'axes.spines.top': True,
              'axes.autolimit_mode': 'data'}  # 'data' or 'round_numbers'
plt.rcParams.update(AxesParams)

TicksParams = {'xtick.bottom': True,
               'xtick.top': True,
               'ytick.left': True,
               'ytick.right': True,
               'xtick.direction': 'in',
               'ytick.direction': 'in',
               'xtick.minor.visible': True,
               'ytick.minor.visible': True,
               'xtick.major.size': 12,
               'xtick.minor.size': 6,
               'xtick.major.width': 1.5,
               'xtick.minor.width': 1.5,
               'xtick.major.pad': 12,
               'xtick.minor.pad': 4,
               'ytick.major.size': 12,
               'ytick.minor.size': 6,
               'ytick.major.width': 1.5,
               'ytick.minor.width': 1.5,
               'ytick.major.pad': 12,
               'ytick.minor.pad': 4,
               'xtick.labelsize': 24,
               'ytick.labelsize': 24}
plt.rcParams.update(TicksParams)

GridParams = {'grid.color': 'b0b0b0',
              'grid.linestyle': '--',
              'grid.linewidth': 0.9,
              'grid.alpha': 1}
plt.rcParams.update(GridParams)

LineParams = {'lines.linewidth': 3,
              'lines.linestyle': '-',
              'lines.marker': None,
              'lines.markerfacecolor': 'auto',
              'lines.markeredgecolor': 'auto',
              'lines.markersize': 16}
plt.rcParams.update(LineParams)


def importdata(path_data):
    # import data
    lnames = []
    dRowData = pd.read_csv(path_data, sep=',', header=None)
    for iColumn in range(0, len(dRowData.columns)):
        temp = dRowData.iloc[0, iColumn]
        lnames.append(temp.strip())
    data = pd.read_csv(path_data, sep=',', header=0, names=lnames)
    return data


plt.clf()
fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111)
data_path = r'data'
list_sheet_thicknesses = list(range(1, 11))

for i, file in enumerate(os.listdir(data_path)):

    if file.endswith('.txt'):
        print(file)
        data = importdata(os.path.join(data_path, file))
        ax.plot(2*data['xPos'] / (list_sheet_thicknesses[i]), data['zEz'] * 100,
                label=str(list_sheet_thicknesses[i]))

ax.set_xlabel('$z$/($t$/2) [1]')
ax.set_ylabel('$\\varepsilon_{\\mathrm{z}}$  [%]')

ax.legend(bbox_to_anchor=(1.04, 1.05), loc='upper left', title='$t$ [mm]', ncol=1) \
    ._legend_box.align = 'left'

plt.savefig('z_strain_distribution.png', dpi=400, bbox_inches='tight', transparent=True)
