import React from 'react';
import {
  Box,
  TextField,
  Button,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
} from '@mui/material';

interface IncomeFormProps {
  formData: any;
  setFormData: (data: any) => void;
  onNext: () => void;
}

const IncomeForm: React.FC<IncomeFormProps> = ({ formData, setFormData, onNext }) => {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onNext();
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
      <Typography variant="h6" gutterBottom>
        Tell us about your income
      </Typography>
      
      <TextField
        fullWidth
        label="Monthly Income (₹)"
        type="number"
        value={formData.monthly_income || ''}
        onChange={(e) =>
          setFormData({
            ...formData,
            monthly_income: parseFloat(e.target.value) || 0,
          })
        }
        margin="normal"
        required
        InputProps={{
          inputProps: { min: 0 }
        }}
      />

      <FormControl fullWidth margin="normal">
        <InputLabel>Approximate Credit Score</InputLabel>
        <Select
          value={formData.credit_score || ''}
          label="Approximate Credit Score"
          onChange={(e) =>
            setFormData({
              ...formData,
              credit_score: e.target.value ? Number(e.target.value) : null,
            })
          }
        >
          <MenuItem value="">Unknown</MenuItem>
          <MenuItem value="300">300-500 (Poor)</MenuItem>
          <MenuItem value="600">600-700 (Fair)</MenuItem>
          <MenuItem value="700">700-750 (Good)</MenuItem>
          <MenuItem value="750">750-800 (Very Good)</MenuItem>
          <MenuItem value="800">800-850 (Excellent)</MenuItem>
        </Select>
      </FormControl>

      <Box sx={{ mt: 3, display: 'flex', justifyContent: 'flex-end' }}>
        <Button
          type="submit"
          variant="contained"
          color="primary"
          disabled={!formData.monthly_income}
        >
          Next
        </Button>
      </Box>
    </Box>
  );
};

export default IncomeForm; 