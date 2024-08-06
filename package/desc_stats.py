import pandas as pd
import numpy as np
import scipy as sc
import statistics
from scipy import stats
from scipy.stats import gmean, hmean
import streamlit as st

class all:
    @staticmethod
    def descriptive_stats(df):
        
        # Compute descriptive statistics
        desc_stats = df.describe()
        count = desc_stats['count']
        std = desc_stats['std']
        mean = desc_stats['mean']
        
        return{
            'mean': desc_stats.loc['mean'],
            'standard_error': std / np.sqrt(count),
            'median': float(np.median(df)),
            'mode': statistics.mode(df), # can xem them vi co the mode co nhieu gia tri
            'std': desc_stats.loc['std'],
            'variance': std ** 2,
            'kurtosis': float(stats.kurtosis(df, bias=False)),
            'skewness': float(stats.skew(df, bias=False)),        
            'range': float(np.ptp(df)),
            'max': desc_stats.loc['max'],
            'min': desc_stats.loc['min'],
            'sum': float(np.sum(df)),
            'count': desc_stats.loc['count'],
            'geometric_mean': float(gmean(df)),
            'harmonic_mean': float(hmean(df)),        
            'average_deviation': float(np.mean(np.abs(df - mean))),        
            'median_abs_deviation': float(stats.median_abs_deviation(df)),        
            'iqr': float(stats.iqr(df)),
            '25%': desc_stats.loc['25%'],
            '50%': desc_stats.loc['50%'],
            '75%': desc_stats.loc['75%'],
            'cv': str(round(stats.variation(df) * 100, 2)) + "%",
        }
        
    @staticmethod
    def single_data():
        # Create input to enter the number of rows
        rows = st.number_input('Nhập số dòng:', min_value=2, value=2)
        
        # Create an empty DataFrame with one column without naming the column
        data = pd.DataFrame(index=range(rows), columns=[None])
        
        with st.expander(f'Nhập dữ liệu cho {rows} dòng'):
            for i in range(rows):
                data.iloc[i, 0] = st.number_input(f'Nhập tần suất tại hàng {i+1}:', key=f'{i}', min_value=0)
        
        data_dict = data.squeeze().to_dict()  # Convert the single column DataFrame to a dictionary
        
        # Convert the dictionary back to a DataFrame
        data_df = pd.DataFrame(list(data_dict.values()), columns=['Giá trị'])
        
        # Calculate descriptive statistics
        desc1 = pd.DataFrame([all.descriptive_stats(data_df['Giá trị'])]).T
        col1, col2 = st.columns(2)
        with col1:
            st.write(data_df)
        with col2:
            st.write(desc1) 
        
        return
        
    @staticmethod    
    def multiple_data():
        col1, col2 = st.columns(2)
        
        with col1:
            # Create input to enter the number of columns
            cols = st.number_input('Nhập số cột:', min_value=2, value=2, max_value=5)  # Increased max_value for more columns
            
        with col2:
            # Create input to enter the number of rows
            rows = st.number_input('Nhập số dòng:', min_value=2, value=2)
            
        # Create column names: first column is "Giá trị", subsequent columns are "Tần suất"
        column_names = ['Giá trị'] + [f'Tần suất {i+1}' for i in range(cols-1)]
        
        # Create empty DataFrame with column names
        data = pd.DataFrame(index=range(rows), columns=column_names)
        
        # Create columns on the interface
        columns = st.columns(cols)
        
        # Display inputs to enter data into DataFrame for each column
        for j in range(cols):
            with columns[j]:
                with st.expander(f'Nhập dữ liệu cho cột {j+1}'):
                    for i in range(rows):
                        if j == 0:
                            data.iloc[i, j] = st.number_input(f'Nhập giá trị tại hàng {i+1}, cột {j+1}:', key=f'{i}_{j}')
                        else:
                            data.iloc[i, j] = st.number_input(f'Nhập tần suất tại hàng {i+1}, cột {j+1}:', key=f'{i}_{j}', min_value=0)
        
        # Tạo danh sách để lưu kết quả phân tách theo từng cột
        expanded_lists = {col: [] for col in column_names[1:]}
        
        # Lặp qua từng hàng trong DataFrame
        for index, row in data.iterrows():
            
            # Lặp qua các cột tần suất
            for col in column_names[1:]:  # Bỏ qua cột đầu tiên "Giá trị"
                
                # Chỉ mở rộng danh sách nếu giá trị tần suất không phải NaN và là số nguyên không âm
                if pd.notna(row[col]) and row[col] > 0:
                    expanded_lists[col].extend([row['Giá trị']] * int(row[col]))
                    
        # Kiểm tra xem có bất kỳ danh sách nào không rỗng
        if any(expanded_lists.values()):
            expanded_df = pd.concat({col: pd.Series(expanded_list) for col, expanded_list in expanded_lists.items()}, axis=1)

            # Tính toán thống kê mô tả cho từng cột và lưu kết quả vào danh sách
            stats_results = []
            
            for col in expanded_df.columns:
                stats_result = all.descriptive_stats(expanded_df[col])
                stats_result['column'] = col  # Thêm tên cột vào kết quả
                stats_results.append(stats_result)
        
            # Tạo DataFrame từ danh sách kết quả thống kê
            stats_df = pd.DataFrame(stats_results).set_index('column')
            st.write(stats_df.T)
            
        return data
